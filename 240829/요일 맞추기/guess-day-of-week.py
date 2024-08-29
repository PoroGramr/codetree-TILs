monthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #각 월별 일수를 저장해둔 리스트
dayWeek = {"Mon" : 0, "Tue" : 1, "Wed" : 2, "Thu" : 3, "Fri" : 4, "Sat" : 5, "Sun" : 6}
dayWeekReverse = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())

days1 = 0
for i in range(0, m1 - 1):
    days1 += monthDays[i]
days1 += d1

days2 = 0
for i in range(0, m2 - 1):
    days2 += monthDays[i]
days2 += d2 

dayDifference = days2 - days1

dayDivide = dayDifference // 7
dayPercent = dayDifference % 7

answer = dayWeekReverse[dayPercent]


print(answer)