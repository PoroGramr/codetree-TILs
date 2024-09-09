"""
문제이해
- 입력
    - N,H,T 
        N : N개의 밭의 N(개수)
        H : 원하는 높이
        T : 원하는 높이로 나와야하는 최소 빈도의 수
    - N개의 밭에 대한 리스트
- 출력
    - 조건을 만족하는 높낮이를 변경할 떄에 최소 비용
아이디어
- N개 밭 리스트를 처음부터 순회하며 탐색해야 함

minCost = sys.maxsize
for i in range(len(data)):# i부터 연속으로 H가 T번 나오게 할때 드는 비용 계산
    cost = 0
    for k in range(T):
        if data[i + k] != H:
            cost += abs(data[i] - H)
    
    mincost = min(cost, mincost)

        

"""
import sys

N,H,T = map(int, input().split())

data = list(map(int, input().split()))

minCost = sys.maxsize

for i in range(len(data) - (T-1)):# i부터 연속으로 H가 T번 나오게 할때 드는 비용 계산
    cost = 0
    for k in range(T):
        if data[i + k] != H:
            cost += abs(data[i + k] - H)
    
    minCost = min(cost, minCost)

print(minCost)