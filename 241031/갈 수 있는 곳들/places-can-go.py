from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v[i][j] = 1

    while q:
        ci,cj = q.popleft()

        for pi, pj in ((0,-1), (0,1), (1,0), (-1,0)):
            ni, nj = ci + pi, cj + pj
            if 0 <= ni < n and 0 <= nj < n and data[ni][nj] == 0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni,nj))

n, k = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

ij = []

for _ in range(k):
    i,j = map(int, input().split())
    ij.append((i-1,j-1))

ans = 0
v = [[0] * n for _ in range(n)]
for ci, cj in ij:
    
    bfs(ci,cj)
for i in range(n):
    for j in range(n):
        if v[i][j] == 1:
            ans += 1

print(ans)