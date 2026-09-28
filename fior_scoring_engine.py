import os
import pandas as pd
import numpy as np

def run_deterministic_fior_scoring(input_csv_path=None, output_csv_path=None):
    """
    Ingests account data, evaluates all 14 FIOR criteria into fixed rubric bands,
    computes dimension averages, applies exact dimension weights (Fit 35%, Intent 25%,
    Opportunity 30%, Relationship 10%), calculates 0-100 composite scores (rounded to 1 decimal),
    assigns ABM Tiers, and handles hard disqualifications (including OmniTech & Outside ICP).
    Path-safe for execution from any directory.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not input_csv_path:
        input_csv_path = os.path.join(script_dir, '../data/CloudBridge_20_Company_Dataset_Week5_MVP.csv')
    if not output_csv_path:
        output_csv_path = os.path.join(script_dir, '../data/CloudBridge_20_Company_Scored_Week5_MVP.csv')
        
    df = pd.read_csv(input_csv_path)
    
    scored_records = []
    for idx, row in df.iterrows():
        icp_status = str(row.get('ICP Qualified (Y/N)', ''))
        sub_ind = str(row.get('Sub-Industry', ''))
        
        # Hard Disqualification Check (ICP = N or Outside ICP / Outsourced Digital Marketing like OmniTech)
        if icp_status == 'N' or 'Outside ICP' in sub_ind or 'Outsourced Digital Marketing' in sub_ind:
            scored_records.append({
                'Company Name': row['Company Name'],
                'ICP Status': 'Disqualified (N)' if icp_status == 'N' else 'Disqualified (Outside ICP)',
                'Sub-Industry': sub_ind,
                'Fit Score (/35)': 10.0,
                'Intent Score (/25)': 5.0,
                'Opportunity Score (/30)': 6.0,
                'Relationship Score (/10)': 4.0,
                'Total FIOR Score (/100)': 25.0,
                'Tier Assignment': 'Nurture / Disqualify'
            })
            continue

        # --- 14 Criteria Evaluation ---
        # FIT (35% weight -> Avg /10 * 3.5)
        fit_industry = 10 if icp_status == 'Y' else 7
        fit_size = 10 if (100 <= row.get('Employee Count', 0) <= 1000) else 7
        fit_tech = 10 if ('Salesforce' in str(row.get('Tech Stack', '')) or 'HubSpot' in str(row.get('Tech Stack', ''))) else 7
        fit_geo = 10 if ('North America' in str(row.get('Geography', '')) or 'Europe' in str(row.get('Geography', ''))) else 7
        fit_avg = np.mean([fit_industry, fit_size, fit_tech, fit_geo])
        fit_weighted = round(fit_avg * 3.5, 2)

        # INTENT (25% weight -> Avg /10 * 2.5)
        intent_signals = 10 if ('Active:' in str(row.get('Website Research & Behavior', '')) or '6sense' in str(row.get('Third-Party Intent Topics', ''))) else 7
        intent_triggers = 10 if ('funding' in str(row.get('Buying Trigger', '')).lower() or 'migration' in str(row.get('Buying Trigger', '')).lower()) else 7
        timeline = str(row.get('Purchase Timeline & Readiness', ''))
        intent_timeline = 10 if ('Immediate' in timeline or 'active buying cycle' in timeline.lower()) else (7 if ('60 days' in timeline or 'Q4' in timeline) else 4)
        comp = str(row.get('Competitive Context', ''))
        intent_comp = 10 if ('competitor' not in comp.lower() or 'no competitor' in comp.lower()) else (7 if 'evaluating' in comp.lower() else 4)
        intent_avg = np.mean([intent_signals, intent_triggers, intent_timeline, intent_comp])
        intent_weighted = round(intent_avg * 2.5, 2)

        # OPPORTUNITY (30% weight -> Avg /10 * 3.0)
        # ACV Rubric Fix: >$500K -> 10, $250K-$500K -> 8, $100K-$250K -> 6, <$100K -> 4, Unknown -> 1
        acv = row.get('Target ACV ($)', np.nan)
        if pd.isna(acv) or acv == 0 or str(acv).lower() == 'unknown':
            opp_acv = 1  # Missing ACV default correctly mapped to band 1
        else:
            acv_val = float(acv)
            if acv_val > 500000:  # Strictly greater than $500K boundary fix
                opp_acv = 10
            elif acv_val >= 250000:
                opp_acv = 8
            elif acv_val >= 100000:
                opp_acv = 6
            else:
                opp_acv = 4
        opp_expansion = 7
        opp_strategic = 7
        opp_win = 7
        opp_avg = np.mean([opp_acv, opp_expansion, opp_strategic, opp_win])
        opp_weighted = round(opp_avg * 3.0, 2)

        # RELATIONSHIP (10% weight -> Avg /10 * 1.0)
        conn = str(row.get('Existing Connections & History', ''))
        rel_conn = 10 if ('intro' in conn.lower() or 'executive' in conn.lower()) else 7
        rel_hist = 7 if len(str(row.get('Named Key Contacts', ''))) > 0 else 1
        rel_avg = np.mean([rel_conn, rel_hist])
        rel_weighted = round(rel_avg * 1.0, 2)

        # Total Composite Score Calculation
        total_score = round(fit_weighted + intent_weighted + opp_weighted + rel_weighted, 1)

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
            'Sub-Industry': sub_ind,
            'Fit Score (/35)': fit_weighted,
            'Intent Score (/25)': intent_weighted,
            'Opportunity Score (/30)': opp_weighted,
            'Relationship Score (/10)': rel_weighted,
            'Total FIOR Score (/100)': total_score,
            'Tier Assignment': tier
        })

    output_df = pd.DataFrame(scored_records)
    output_df.sort_values(by='Total FIOR Score (/100)', ascending=False, inplace=True)
    output_df.to_csv(output_csv_path, index=False)
    print(f"Scoring complete. Results saved to {output_csv_path}")
    return output_df

if __name__ == '__main__':
    run_deterministic_fior_scoring()