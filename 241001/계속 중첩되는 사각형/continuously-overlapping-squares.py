n = int(input())

data= [[0 for _ in range (200)] for _ in range(200)]
count = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1,y1,x2,y2 = x1 +100, y1 + 100, x2 + 100, y2 + 100
    if i % 2 == 0: # 빨간색
        for y in range(y1, y2):
            for x in range(x1, x2):
                data[y][x] = 1
    else:           # 파란색
        for y in range(y1,y2):
            for x in range(x1,x2):
                data[y][x] = 2

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 2:
            count += 1
print(count)