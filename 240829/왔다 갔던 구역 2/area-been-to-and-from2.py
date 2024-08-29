data = [0] * 1000

n = int(input())
currentX = 499
for _ in range(n):
    x, direction = map(str, input().split())
    x = int(x)

    if direction == "R":
        # 오른쪽으로 이동하는 경우
        for i in range(currentX, currentX + x):
            data[i] += 1
        currentX += x  # 현재 위치 업데이트
        
    elif direction == "L":
        # 왼쪽으로 이동하는 경우
        for i in range(currentX - 1, currentX - x - 1, -1):
            data[i] += 1
        currentX -= x  # 현재 위치 업데이트

answer = 0
for i in data:
    if i >= 2:
        answer += 1

print(answer)