"""
- 문제 이해
    - 마라톤은 총 N개의 체크포인트로 구성, 
    1번부터 순서대로 체크포인트를 거친 후 N번 체크포인트까지 도달해야 완주

    - 개발자 A는 체크포인트 한개만 건너뛰고 완주하려함
    - 이때 개발자A가 움직이는 최소거리를 구하여야 함
    - 이동거리 계산은 두 지점 간의 거리를 택시 거리로 계산

- 아이디어
    - 처음시작 지점(1번 체크포안트)과 마지막 N번째 체크포인트는 무조건 거쳐야 함
    - 2번 체크포인트 부터 N-1번쨰 체크포인트까지 에서 한번만 스킵할 수 있음
    - for문을 통해 한 체크포인트를 뺴고 총 거리를 계산하며 최소값을 업데이트해보자
"""
import sys

n = int(input())

xyData = []

for i in range(n):
    x,y = map(int, input().split())
    xyData.append([x, y])

# [[0, 0], [8, 3], [11, -1], [10, 0]]

# 파이썬에서 가능한 최대 정수값 지정
minLen = sys.maxsize

# 첫번째 지점과 마지막 지점 제외
for k in range(1, n-1):
    currentMin = 0
    for j in range(1, n):

        # 상단 for문에서 선택된 N번째 체크포인트는 스킵 
        if j == k:
            continue
        
        # 만약 이전 체크포인트가 스킵된 체크 포인트라면
        if j-1 == k:
            currentMin += abs(xyData[j-2][0] - xyData[j][0]) + abs(xyData[j-2][1] - xyData[j][1])
        
        # 일반적인 이전 체크포인트와의 거리 계산
        else:
            currentMin += abs(xyData[j-1][0] - xyData[j][0]) + abs(xyData[j-1][1] - xyData[j][1])

    # 최소값을 계속해서 비교
    minLen = min(minLen, currentMin)

# 출력
print(minLen)