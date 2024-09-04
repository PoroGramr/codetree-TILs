import sys

n = int(input())

homeData = list(map(int, input().split()))

# 최소값 초기값을 세팅
minValue = -sys.maxsize

for i in range(n):
    moveSum = 0

    # 이동거리 계산
    for k in range(n):
        moveSum += abs((i - k)) * homeData[k]

    # 첫번째 루프에서는 최소값을 초기화해줌
    if i == 0:
        minValue = moveSum
        continue

    # 그 이후부터 최소값을 탐색
    if moveSum < minValue:
        minValue = moveSum


print(minValue)