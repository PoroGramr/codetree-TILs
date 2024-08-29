data = [0] * 100

n = int(input())
currentX = 49
for _ in range(n):
    x, point = map(str, input().split())
    x = int(x)
    storeX = currentX
    cac = 0
    if point == "R":
        for i in range(currentX, storeX + x):
            data[i] += 1
            cac += 1
    else:
        for i in range(currentX, storeX - x, -1):
            data[i] += 1
            cac -= 1
    
    storeX += cac
    currentX += cac

answer = 0
for i in data:
    if i >= 2:
        answer += 1

print(answer)