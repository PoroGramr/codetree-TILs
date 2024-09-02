data = [[0] * 200 for _ in range(200)]

n = int(input())

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + 100, y1 + 100
    x2, y2 = x1 + 8, y1 + 8

    for y in range(y1, y2):
        for x in range(x1, x2):
            data[y][x] = 1


answer = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
                answer += 1

print(answer)