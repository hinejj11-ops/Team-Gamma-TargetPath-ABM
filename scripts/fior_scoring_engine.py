import pandas as pd
import numpy as np

def run_deterministic_fior_scoring(input_csv_path, output_csv_path):
    """
    Ingests the classified account data (or enriched dataset), applies deterministic 
    FIOR scoring rules, weights dimensions, computes total composite score (0-100), 
    assigns ABM Tiers, and handles hard disqualifications.
    """
    df = pd.read_csv(input_csv_path)
    
    scored_records = []
    for idx, row in df.iterrows():
        # Hard Disqualification Check (Step 0 / ICP Gate)
        if row.get('ICP Qualified (Y/N)') == 'N':
            scored_records.append({
                'Company Name': row['Company Name'],
                'ICP Status': 'Disqualified (N)',
                'Sub-Industry': row['Sub-Industry'],
                'Fit Score (/35)': 10.0,
                'Intent Score (/25)': 5.0,
                'Opportunity Score (/30)': 6.0,
                'Relationship Score (/10)': 4.0,
                'Total FIOR Score (/100)': 25.0,
                'Tier Assignment': 'Nurture / Disqualify'
            })
            continue

        # Deterministic Sub-score Calculation based on qualitative parameters
        # 1. Fit Score Component (Out of 35)
        fit_base = 32.0 if row.get('ICP Qualified (Y/N)') == 'Y' else 24.0
        
        # 2. Intent Score Component (Out of 25)
        timeline = str(row.get('Purchase Timeline & Readiness', ''))
        if 'Immediate' in timeline or 'Active buying cycle' in timeline:
            intent = 22.0
        elif 'Near-term' in timeline:
            intent = 18.0
        elif 'Long-term' in timeline:
            intent = 12.0
        else:
            intent = 8.0
            
        # 3. Opportunity Score Component (Out of 30)
        acv = float(row.get('Target ACV ($)', 150000))
        if acv >= 500000:
            opp = 27.0
        elif acv >= 250000:
            opp = 22.0
        elif acv >= 100000:
            opp = 18.0
        else:
            opp = 12.0
            
        # 4. Relationship Score Component (Out of 10)
        champ = str(row.get('Champion Status', ''))
        if 'Strong Champion' in champ or 'Identified' in champ:
            rel = 8.5
        elif 'Emerging Champion' in champ or 'Moderate Champion' in champ:
            rel = 6.0
        else:
            rel = 4.0
            
        # Total Composite Score Calculation
        total_score = round(fit_base + intent + opp + rel, 2)
        
        # Tier Assignment Thresholds
        if total_score >= 80:
            tier = "Tier 1 (1:1 ABM)"
        elif total_score >= 60:
            tier = "Tier 2 (1:Few ABM)"
        elif total_score >= 40:
            tier = "Tier 3 (1:Many ABM)"
        else:
            tier = "Nurture / Disqualify"
            
        scored_records.append({
            'Company Name': row['Company Name'],
            'ICP Status': row.get('ICP Qualified (Y/N)'),
            'Sub-Industry': row['Sub-Industry'],
            'Fit Score (/35)': fit_base,
            'Intent Score (/25)': intent,
            'Opportunity Score (/30)': opp,
            'Relationship Score (/10)': rel,
            'Total FIOR Score (/100)': total_score,
            'Tier Assignment': tier
        })
        
    output_df = pd.DataFrame(scored_records)
    output_df.sort_values(by='Total FIOR Score (/100)', ascending=False, inplace=True)
    output_df.to_csv(output_csv_path, index=False)
    print(f"Scoring complete. Results saved to {output_csv_path}")
    return output_df

# Execute script on Week 5 dataset
scored_portfolio = run_deterministic_fior_scoring(
    'CloudBridge_20_Company_Dataset_Week5_MVP.csv', 
    'CloudBridge_20_Company_Scored_Week5_MVP.csv'
)
print(scored_portfolio[['Company Name', 'ICP Status', 'Total FIOR Score (/100)', 'Tier Assignment']].head(10))
print("\nNew Portfolio Tier Distribution:\n", scored_portfolio['Tier Assignment'].value_counts())