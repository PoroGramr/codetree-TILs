from collections import deque

def bfs():
    q = deque()
    v = [([0] * n) for _ in range(m)]
    v[0][0] = 1
    q.append((0,0))

    while q:
        
        cx,cy = q.popleft()

        if (cx, cy) == (n-1, m-1):
            return 1

        for px, py in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + px, cy + py

            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and v[nx][ny] == 0:
                v[nx][ny] = 1
                q.append((nx,ny))
    return 0
    
    


n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

answer = bfs()
print(answer)