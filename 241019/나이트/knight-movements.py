from collections import deque


def bfs(y,x):
    q = deque()
    q.append((y,x))

    while q:
        cy, cx = q.popleft()

        if cy == r2 - 1 and cx == c2 - 1:
            return data[cy][cx]
        
        for py, px in ((-1, -2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)):
            ny, nx = cy + py, cx + py
            if 0 <= ny < n and 0 <= nx < n and (data[ny][nx] == 0 or data[ny][nx] == 1) :
                q.append((ny,nx))
                data[ny][nx] = data[cy][cx] + 1

    return -1

n = int(input())

r1, c1, r2, c2 = map(int, input().split())
data = [[-1] * n for _ in range(n)]
data[r2 - 1][c2 - 1] = 0

ans = bfs(r1-1,c1-1)

print(ans)