# Presentation script (about 6 minutes)

**0:00 Intro.** I'm Safrah, a Data Analytics intern at AnalystLab Africa. I built a complaint monitoring dashboard on 62,516 Bank of America complaints from the CFPB, 2017 to 2023. A complaint is a consumer-reported issue, not proof of misconduct.

**0:30 Data work.** I checked structure, duplicates, missing values and dates. Complaint ID is unique, no rows were removed. 1,494 blank Timely response values are complaints still in progress, so I did not count them as No. Date received minus Date submitted is the CFPB forwarding interval, not company response time.

**1:30 Overview page.** 62,516 complaints, 96.06% timely, average forwarding interval 1.22 days, median 0, 1,494 in progress. Volume rose from 7,872 in 2018 to 12,953 in 2022, up 64.5%.

**2:30 Product and Issue page.** Checking/savings and credit/prepaid cards are 65.6% of complaints. Managing an account is the top issue: 24.2% of all complaints, 60.9% of checking/savings.

**3:30 Company Response page.** 65.7% closed with explanation, 23.5% with monetary relief. Timely response fell from 99%+ to 89.0% in 2021. Slicers: show Year 2021.

**4:30 Timeline page.** 79.4% forwarded same day, but 435 took over 30 days, longest 275. Referral channel averages 3.3 days.

**5:15 Validation.** I rechecked totals, timely % and average interval in Excel and Python; all matched.

**5:35 Recommendations.** Review account-servicing complaints; monitor timely % monthly and investigate 2021; review the referral channel and long cases; refresh when open complaints close.

**5:55 Limits and close.** Partial years, one company, no narratives. Thank you.
