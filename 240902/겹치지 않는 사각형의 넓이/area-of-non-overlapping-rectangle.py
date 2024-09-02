data = [[0] * 2000 for _ in range(2000)]

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2  = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000

for i in range(y1, y2):
    for j in range(x1, x2):
        data[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2  = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000

for i in range(y1, y2):
    for j in range(x1, x2):
        data[i][j] = 1


x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2  = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000

for i in range(y1, y2):
    for j in range(x1, x2):
        data[i][j] = 0

answer = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
            answer += 1

print(answer)