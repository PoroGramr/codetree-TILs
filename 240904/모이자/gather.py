import sys

n = int(input())

homeData = list(map(int, input().split()))

minValue = -sys.maxsize

for i in range(n):
    moveSum = 0
    for k in range(n):
        moveSum += abs((i - k)) * homeData[k]

    if i == 0:
        minValue = moveSum
        continue

    if moveSum < minValue:
        minValue = moveSum


print(minValue)