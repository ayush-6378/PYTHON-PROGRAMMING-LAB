from datetime import date
d1=(4,5,2026)
d2=(25,5,2026)
date1=date(d1[2],d1[1],d1[0])
date2=date(d2[2],d2[1],d2[0])
delta=abs(date2-date1)
print(f"number of days : {delta.days}")
