#!/usr/bin/env python3
"""Reproducible, provisional TargetPath FIOR scorer. Standard library only.
Run: python tools/score_v1_1.py --input data/20_Company_Dataset_Iteration7.csv --out-dir validation/local_run
Never reads validation answer keys. Human review is mandatory before release.
"""
import argparse, csv, datetime as dt, math, pathlib, re
ASOF=dt.date(2026,10,11)
PROFILES=[
 ({"Cloud Infrastructure","Enterprise Software","IT Services & Consulting"},{"Cybersecurity & Compliance","Cloud Infrastructure & DevOps"}),
 ({"FinTech SaaS","Enterprise Software"},{"FinTech Solutions"}),
 ({"HealthTech Solutions","Enterprise Software","Cloud Infrastructure"},{"HealthTech SaaS"}),
]
def date(s):
 try: return dt.date.fromisoformat(s) if s else None
 except ValueError: return None
def age(s): return (ASOF-date(s)).days if date(s) else None
def match(s,p): return bool(re.search(p,s or "",re.I))
def months_after(n):
 y=ASOF.year+(ASOF.month-1+n)//12;m=(ASOF.month-1+n)%12+1
 import calendar
 return dt.date(y,m,min(ASOF.day,calendar.monthrange(y,m)[1]))
def tier(v): return "Tier 1" if v>=80 else "Tier 2" if v>=60 else "Tier 3" if v>=40 else "Nurture / Disqualify"
def total(vals):
 parts=[]
 for lo,hi,mul in [(0,4,3.5),(4,8,2.5),(8,12,3.0),(12,14,1.0)]:
  a=[v for v in vals[lo:hi] if v is not None]
  parts.append(sum(a)/len(a)*mul if a else 0)
 return parts,math.floor(sum(parts)+0.5)
def score(x):
 v=[None]*14; ev=[];flags=[]
 def put(i,val,fields,rule):
  v[i-1]=val
  ev.append({"Company":x["Company Name"],"Criterion":f"C{i}","Score":"NS" if val is None else val,"Evidence":" | ".join(f"{f}={x.get(f,'') or '[blank]'}" for f in fields),"Rule":rule,"Confidence":"Low" if val is None else "High"})
 ind=x["Industry"];sub=x["Sub-Industry"]
 full=any(ind in a and sub in b for a,b in PROFILES)
 put(1,2 if match(sub,"Outside ICP") else 10 if full else 8 if any(ind in a for a,b in PROFILES) else 4,["Industry","Sub-Industry"],"same-profile ICP and exclusion")
 emp=int(x["Employee Count"]);rev=float(x["Annual Revenue ($M)"])
 inside=lambda n,l,h:l<=n<=h
 near=lambda n,l,h:l*.75<=n<=h*1.25
 put(2,10 if inside(emp,150,750) and inside(rev,50,200) else 8 if near(emp,150,750) and near(rev,50,200) and (inside(emp,150,750) or inside(rev,50,200)) else 6 if near(emp,150,750) and near(rev,50,200) else 4 if near(emp,150,750) or near(rev,50,200) else 2,["Employee Count","Annual Revenue ($M)"],"ICP size anchors")
 keys=["CRM / Sales Engagement","Cloud Infrastructure","Data / Analytics"]
 t=[x[k] for k in keys]
 hits=[match(t[0],"Salesforce|HubSpot Enterprise|Apollo"),match(t[1],"AWS|Azure|GCP"),match(t[2],"Snowflake|Databricks|Segment")]
 preferred=match(x["Intent / ABM Platform"],"6sense|Demandbase|ZoomInfo Enterprise") and match(x["Marketing Automation"],"Marketo|Pardot")
 incompatible=match(t[1],"legacy proprietary|no cloud connector")
 put(3,2 if incompatible else None if any(not z or z=="Unknown" for z in t) else 10 if all(hits) and preferred else 8 if all(hits) else 4 if any(hits) else 2,keys+["Intent / ABM Platform","Marketing Automation"],"required technology coverage; preferred distinction")
 req=["SOC 2 Type II","ISO 27001"]+(["GDPR Ready"] if "Europe" in x["Geography"] else [])+(["HIPAA Ready"] if sub=="HealthTech SaaS" else [])
 c=[x[k] for k in req]
 put(4,None if any(not z or z=="Unknown" for z in c) else 4 if "No" in c else 10,["Geography"]+req,"applicable compliance; unknown NS")
 sig=[];sk=[]
 for i in range(1,5):
  typ=x[f"Intent Signal {i} Type"];dat=x[f"Intent Signal {i} Date"]
  sk += [f"Intent Signal {i} Type",f"Intent Signal {i} Date"]
  a=age(dat)
  if typ and not match(typ,"^Verified no") and a is not None and 0<=a<=90:sig.append((typ,a))
 n30=len({t for t,a in sig if a<=30});n90=len({t for t,a in sig})
 negative=all(match(x[f"Intent Signal {i} Type"],"^Verified no") for i in range(1,5))
 put(5,10 if n30>=3 else 8 if n30>=2 or n90>=3 else 6 if n30>=1 or n90>=2 else 4 if n90 else 2 if negative else None,sk,"distinct positive signal types, dated")
 trig=[t.strip() for t in x["Trigger Type"].split(";") if t.strip()]
 dates=[z.strip() for z in x["Trigger Date"].split(";")]
 events=[(t,age(dates[i] if i<len(dates) else "")) for i,t in enumerate(trig)]
 six=[(t,a) for t,a in events if a is not None and 0<=a<=183]
 relevant=lambda t:match(t,"funding|migration|platform upgrade|expansion|compliance|regulatory|leadership|acquisition|merger")
 put(6,None if not trig else 2 if match(trig[0],"Verified no trigger|No trigger identified") else 10 if len({t for t,a in six})>=2 and any(relevant(t) for t,a in six) else 8 if any(relevant(t) for t,a in six) else 6 if six or any(a is not None and 0<=a<=365 and relevant(t) for t,a in events) else 4,["Trigger Type","Trigger Date"],"dated relevant triggers")
 if match(x["Trigger Type"],"leadership"):flags.append("leadership change")
 tl=x["Purchase Timeline & Readiness"]
 put(7,10 if match(tl,"RFP|active buying cycle") else 8 if match(tl,"near-term") else 6 if match(tl,"6 to 12 months") else 4 if match(tl,"long-term|12\\+ months") else 2,["Purchase Timeline & Readiness"],"stated timeline")
 status=x["Incumbent Contract Status"];sat=x["Incumbent Satisfaction"];renew=date(x["Contract Renewal Date"])
 mo=(renew-ASOF).days/30.4375 if renew else None
 put(8,8 if status=="No incumbent" else None if status=="Unknown" else 2 if status=="Locked" and (mo is None or mo>=12) else 10 if sat=="Dissatisfied" else 6 if status=="Locked" and mo is not None and mo<=6 else 4,["Incumbent Contract Status","Incumbent Satisfaction","Contract Renewal Date"],"structured incumbent; unknown status NS")
 if status=="Unknown":flags.append("unknown contract status")
 acv=int(x["Target ACV ($)"])
 put(9,10 if acv>500000 else 8 if acv>=250000 else 6 if acv>=100000 else 4,["Target ACV ($)"],"ACV anchors")
 products=len([a for a in x["Applicable TargetOrate Products"].split(";") if a.strip()])
 units=len([a for a in x["Departments / Units in Scope"].split(";") if a.strip()])
 put(10,10 if products>=3 and units>=2 else 8 if products>=2 and units>=2 else 6 if products>=2 or units>=2 else 4,["Applicable TargetOrate Products","Departments / Units in Scope"],"products and business units")
 n=sum([rev>=100 or emp>=500,bool(x["Referenceability Evidence"]),bool(x["Partnership Ecosystem Evidence"])])
 put(11,10 if n==3 else 8 if n==2 else 6 if n==1 else 2,["Annual Revenue ($M)","Employee Count","Referenceability Evidence","Partnership Ecosystem Evidence"],"reference-list market leader proxy")
 budget=match(x["Budget Status"],"^Confirmed")
 favorable=status=="No incumbent" or sat=="Dissatisfied" or (status=="Locked" and mo is not None and mo<=6)
 win=budget # conditional client benchmark, not standalone proof
 factors=sum([budget,favorable,win])
 put(12,10 if factors==3 else 8 if factors==2 and budget else 6 if factors==2 or budget else 4 if factors==1 else 2,["Budget Status","Incumbent Contract Status","Incumbent Satisfaction","Contract Renewal Date"],"conditional historical win rate, budget, competition")
 rel=x["Existing Connections & History"];roleage=age(x["Role Verification Date"])
 r=2 if match(rel,"cold account") else 8 if match(rel,"warm intro via executive") else 6 if match(rel,"past customer at former employer") else 4 if match(rel,"conference|webinar|nurture") else 6 if rel else None
 if roleage is not None and roleage>183:
  r=min(r,6) if r is not None else None;flags.append("stale role")
 put(13,r,["Existing Connections & History","Named Key Contacts","Role Verification Date"],"relationship evidence precedence")
 ch=x["Champion Status"];cust=x["Customer Status"]
 put(14,8 if match(cust,"Former customer - good") else 3 if match(cust,"unhappy churn") else 10 if match(ch,"actively pushing|advocating internally") else 8 if match(ch,"Emerging|Moderate") else 6 if x["Last Meeting / Demo / Event Date"] else 4 if match(rel,"webinar|nurture") else 2,["Customer Status","Champion Status","Last Meeting / Demo / Event Date","Existing Connections & History"],"customer/champion precedence")
 dims,t=total(v);low=total([2 if z is None else z for z in v])[1];high=total([10 if z is None else z for z in v])[1]
 if tier(low)!=tier(high):flags.append("NS tier sensitivity")
 if any(abs(t-b)<=2 for b in [40,60,80]):flags.append("near tier boundary")
 if tier(t)=="Tier 1":flags.append("Tier 1 investment")
 if v[0]==2 and v[1]==2:flags.append("outside ICP and size")
 band=0
 if status=="Locked":
  band=3 if renew is None or renew>months_after(24) else 2 if renew>=months_after(12) else 1
  if sat=="Satisfied":band=min(3,band+1)
  if sat=="Dissatisfied":band=max(1,band-1)
 if band==3:flags.append("competitive lock disqualification")
 if band==2:flags.append("competitive lock cap")
 final="Disqualified (Competitive Lock)" if band==3 else "Tier 3" if band==2 and t>=60 else tier(t)
 out={"Company Name":x["Company Name"],**{f"C{i+1}":"NS" if z is None else z for i,z in enumerate(v)},"Fit":f"{dims[0]:.3f}","Intent":f"{dims[1]:.3f}","Opportunity":f"{dims[2]:.3f}","Relationship":f"{dims[3]:.3f}","Composite":t,"Score Implied Tier":tier(t),"Gate Band":band or "n/a","Final Tier":final,"NS Low":low,"NS High":high,"Review Status":"Review" if flags else "Acceptable","Review Reasons":"; ".join(flags),"Approval":"PROVISIONAL"}
 return out,ev
def write(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",newline="",encoding="utf-8") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--out-dir",required=True);a=p.parse_args()
 with open(a.input,newline="",encoding="utf-8-sig") as f:rows=list(csv.DictReader(f))
 assert len(rows)==20 and len({x["Company Name"] for x in rows})==20,"Expected 20 unique accounts"
 scored=[score(x) for x in rows];out=pathlib.Path(a.out_dir)
 write(out/"portfolio_PROVISIONAL.csv",[x for x,_ in scored])
 write(out/"criterion_evidence.csv",[e for _,a in scored for e in a])
 print(f"Processed {len(rows)} accounts, {sum(len(a) for _,a in scored)} criteria; all results PROVISIONAL")
if __name__=="__main__":main()
