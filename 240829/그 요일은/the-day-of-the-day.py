"""
두 날짜 사이의 일수를 계산한 뒤
제시된 처음 날짜의 요일은 월요일
그중 입력으로 받은 요일의 등장 횟수를 구하라

일단 두번쨰로 제시된 날짜의 요일을 구하는 것이 우선.

"""
monthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #각 월별 일수를 저장해둔 리스트
dayWeek = {"Mon" : 0, "Tue" : 1, "Wed" : 2, "Thu" : 3, "Fri" : 4, "Sat" : 5, "Sun" : 6}
dayWeekReverse = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())
inputDay = input()
inputDay = dayWeek[inputDay]

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


secondDayWeek = dayWeekReverse[dayPercent]
answer = 0
if inputDay < dayPercent:
    answer += 1

answer += dayDivide

print(answer)