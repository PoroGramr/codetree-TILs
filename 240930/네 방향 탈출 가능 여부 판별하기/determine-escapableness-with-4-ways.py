from collections import deque

def bfs():
    q = deque()
    v = [([0] * n) for _ in range(m)]
    v[0][0] = 1
    q.append((0,0))

    while q:
        
        cy,cx = q.popleft()

        if (cy,cx) == (n-1, m-1):
            return 1

        for px, py in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + px, cy + py

            if 0 <= nx < m and 0 <= ny < n and data[ny][nx] == 1 and v[ny][nx] == 0:
                v[nx][ny] = 1
                q.append((ny,nx))
    return 0
    
    


n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

answer = bfs()
print(answer)