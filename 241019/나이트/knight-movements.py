from collections import deque


def bfs(y,x):
    q = deque()
    q.append((y,x))
    count = 0
    while q:
        cy, cx = q.popleft()
        if cy == r2 -1 and cx == c2 - 1:
            return count
        for py, px in ((-1, -2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)):
            ny, nx = cy + py, cx + py
            if 0 <= ny < n and 0 <= nx < n and (data[ny][nx] == 0 or data[ny][nx] == 1) :
                q.append((ny,nx))


n = int(input())

r1, c1, r2, c2 = map(int, input().split())
data = [[0] * n for _ in range(n)]
data[r2 - 1][c2 - 1] = 1

ans = bfs(r1,c1)

print(ans)