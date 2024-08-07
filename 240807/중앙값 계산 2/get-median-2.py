n = int(input())
inputData = list(map(int, input().split(" ")))
data = []

for i in range(n):
    data.append(inputData[i])
    data.sort()
    if (i + 1) % 2 != 0:
        a = len(data) // 2
        print(data[a], end=" ")