"""Independent verification of Week 4 dashboard KPIs.
Run: python3 -I verification_script.py Consumer_Complaints.xlsx
"""
import sys, pandas as pd
df = pd.read_excel(sys.argv[1], sheet_name="Data")
df["Complaint ID"] = df["Complaint ID"].astype(str)
sub, rec = pd.to_datetime(df["Date submitted"]), pd.to_datetime(df["Date received"])
df["Year"] = sub.dt.year
df["Interval"] = (rec - sub).dt.days
tr = df["Timely response?"]
yes, no = (tr == "Yes").sum(), (tr == "No").sum()
print("Total complaints:", df["Complaint ID"].nunique(), "| duplicates:", df["Complaint ID"].duplicated().sum())
print("Timely %:", round(100*yes/(yes+no), 2), "| valid base:", yes+no, "| blanks:", tr.isna().sum())
print("In progress:", (df["Company response to consumer"] == "In progress").sum())
print("Interval avg/median/max:", round(df["Interval"].mean(), 2), df["Interval"].median(), df["Interval"].max())
print("Same-day %:", round(100*(df["Interval"] == 0).mean(), 1), "| >30 days:", (df["Interval"] > 30).sum())
print("\nComplaints by year:\n", df.groupby("Year").size())
print("\nYoY %:\n", (df.groupby("Year").size().pct_change()*100).round(1))
print("\nTimely % by year:\n", (df.assign(y=tr == "Yes")[tr.notna()].groupby("Year")["y"].mean()*100).round(1))
print("\nProduct share %:\n", (df["Product"].value_counts(normalize=True)*100).round(1))
print("\nResponse distribution:\n", df["Company response to consumer"].value_counts())
