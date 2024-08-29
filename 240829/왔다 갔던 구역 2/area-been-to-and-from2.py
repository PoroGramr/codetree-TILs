# 이동 기록 리스트, 왼쪽과 오른쪽 넉넉하게 확보
data = [0] * 1000

# 초기 위치 설정 (중간을 0으로 보기 위해 500으로 설정)
n = int(input())
currentX = 500

# 명령에 따른 이동
for _ in range(n):
    x, direction = input().split()
    x = int(x)
    
    if direction == "R":
        # 오른쪽으로 이동하는 경우, 끝점은 포함하지 않음
        for i in range(currentX, currentX + x):
            data[i] += 1
        currentX += x  # 현재 위치 업데이트
        
    elif direction == "L":
        # 왼쪽으로 이동하는 경우, 끝점은 포함하지 않음
        for i in range(currentX, currentX - x, -1):
            data[i] += 1
        currentX -= x  # 현재 위치 업데이트

# 2번 이상 지나간 구간 계산
answer = 0
for count in data:
    if count >= 2:
        answer += 1

print(answer)