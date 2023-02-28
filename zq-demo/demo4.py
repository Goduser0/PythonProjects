# Noel Stallworth
# Time: 2021-7-20  15:15
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input("day:\n"))

rn=[31,29,31,30,31,30,31,31,30,31,30,31]
frn=[31,28,31,30,31,30,31,31,30,31,30,31]
ans=0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    for i in range(month-1):
        ans+=rn[i]
    ans += day
else :
    for i in range(month-1):
        ans+=frn[i]
    ans += day

print(ans)