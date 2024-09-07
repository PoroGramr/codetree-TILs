n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


maxCnt = 0
for i in range(n):
    for k in range(0, n-2):
        maxCnt = max(maxCnt, (data[i][k] + data[i][k+1] + data[i][k+2]))

print(maxCnt)