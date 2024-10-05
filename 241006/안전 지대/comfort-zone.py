import sys
sys.setrecursionlimit(10**5)  # 재귀 깊이 제한을 1,000,000으로 설정


def dfs(y,x,k):
    v[y][x] = 1

    for py, px in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + py, x + px
        if 0 <= ny < N and 0 <= nx < M and data[ny][nx] > k and v[ny][nx] == 0:
            dfs(ny,nx,k)
    
    return True
    

N,M = map(int, input().split())

data = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)




# data를 탐색하며 최대 k 값을 찾음
bigK = float("-inf")
for t in data:
    t= max(t)
    bigK = max(bigK,t)
answer = []

# k의 값을 1부터 bigK까지 순회
for k in range(1,bigK+1):
    
    # 안전 영역 수 카운트
    ct = 0
    
    # 루프를 돌 떄 마다 v를 초기화 
    v = [[0 for _ in range(M)] for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if data[n][m] > k and v[n][m] == 0:
                # 만약 안전영역이 가능한 구역을 만난다면 k+1
                if dfs(n,m,k):
                    ct += 1

    # answer라는 리스트에 k,안전영역의 수를 삽입            
    answer.append([k,ct])

# 안전영역의 수가 큰 값부터 정렬하돼, k의 값은 작은 순으로 정렬
answer.sort(key = lambda x:(-x[1], x[0]))

# 첫번째 요소를 출력하면 정답
print(answer[0][0], answer[0][1])