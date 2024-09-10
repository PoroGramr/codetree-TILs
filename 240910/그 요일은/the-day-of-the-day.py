"""
두 날짜의 1/1 부터의 날짜수를 계산
2024년 m2월 d2 - 2024년 m1월 d1 을 하면 두 날짜 사이의 일수가 나온다.

1월 1일이 월요일이므로 
weekDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ] 를 통해
A 요일의 인덱스 값을 구한 뒤

만약 A 요일의 인덱스 값이  두날짜의 차이 % 7 한 것보다 크다면 
    두날짜의 차이 //7 + 1
아니라면
    두날짜의 차이 // 7
"""

# 각 월별 일수 저장 # 인덱싱을 편하게 하기 위해 0번쨰 요소에는 None 삽입
monthDays = [None, 31,29,31,30,31,30,31,31,30,31,30,31]

# 입력으로 들어올 요일의 인덱스를 구하기 위해 각 요일이 문자열로 들어있는 리스트 생성
weekDay = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]

m1, d1, m2, d2 = map(int,input().split())
checkWeek = input()

# 입력으로 받은 요일의 인덱스를 저장
countWeek = 0
for k in range(len(weekDay)):
    if checkWeek == weekDay[k]:
        countWeek = k

# 입력으로 받은 첫번째 날짜의 1/1부터 지난 날의 수를 계산
days1 = 0

# 만약 1월이라면 일수만 저장
if m1 == 1:
    days1 += d1

# 1월이 아닐경우에 계산
else:
    for i in range(1, m1):
        days1 +=  monthDays[i]
    days1 += d1

# 입력으로 받은 두번째 날짜의 1/1부터 지난 날의 수를 계산
days2 = 0

# 만약 1월이라면 일수만 저장
if m2 == 1:
    days2 += d2

# 1월이 아닐경우에 계산
else:
    for i in range(1, m2):
        days2 +=  monthDays[i]
    days2 += d2

# 입력된 두 날짜들의 차이 계산
daysMinus = days2 - days1

answer = 0

# 입력으로 받은 요일을 카운트하기 위해 7로 나누기
answer += daysMinus // 7

# 입력으로 받은 요일을 가장 마지막주에 거쳤는지 안거쳤는지 확인 후 정답 출력
if (daysMinus % 7) < countWeek:
    print(answer)
else:
    print(answer + 1)