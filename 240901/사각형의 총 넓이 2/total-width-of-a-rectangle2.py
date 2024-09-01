# data = [[0] * 200 ] * 200

data = [[0] * 200 for _ in range(200)]


n = int(input())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100 
    for a in range(y1, y2):
        for b in range(x1, x2):
            data[a][b] = 1

answer = 0
for a in range(len(data)):
    for b in range(len(data[0])):
        if data[a][b] == 1:
            answer += 1

print(answer)