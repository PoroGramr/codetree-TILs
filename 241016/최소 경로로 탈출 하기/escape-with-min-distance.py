from collections import deque

def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q:
        cy, cx = q.popleft()

        for py, px in ((0,-1), (0,1), (1,0), (-1,0)):
            ny , nx = cy + py, cx + px
            if 0 <= ny < n and 0 <= nx < m and data[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny,nx))
                v[ny][nx] = v[cy][cx] + 1
    print(v)

    return v[n-1][m-1]
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

v = [[0] * m for _ in range(n)]

ans = bfs(0,0)

print(ans)