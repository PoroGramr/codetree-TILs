monthDays = [None, 31,29,31,30,31,30,31,31,30,31,30,31]
weekDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]

m1, d1, m2, d2 = map(int,input().split())
checkWeek = input()
countWeek = ""
for k in range(len(weekDay)):
    if checkWeek == weekDay[k]:
        countWeek = k


days1 = 0

if m1 == 1:
    days1 += d1

else:
    for i in range(1, m1):
        days1 +=  monthDays[i]
    days1 += d1

days2 = 0

if m2 == 1:
    days2 += d2

else:
    for i in range(1, m2):
        days2 +=  monthDays[i]
    days2 += d2

daysMinus = days2 - days1

answer = 0

answer += daysMinus // 7

if (daysMinus % 7) < countWeek:
    print(answer)
else:
    print(answer + 1)