n = int(input())
data = list(map(int, input().split()))

answer = float("inf")

for k in range(n): # 모일 집
    length = 0
    for s in range(n): # 이동할 거리 계산
        length += (abs(s - k)) * data[s]
    answer = min(answer, length)

print(answer)