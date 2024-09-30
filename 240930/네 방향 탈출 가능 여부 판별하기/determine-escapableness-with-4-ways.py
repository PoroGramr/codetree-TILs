from collections import deque

def bfs():
    q = deque()
    v = [([0] * m) for _ in range(n)]
    v[0][0] = 1
    q.append((0,0))

    while q:
        
        cy,cx = q.popleft()

        if (cy,cx) == (n-1, m-1):
            return 1

        for py,px in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx =  cy + py, cx + px

            if 0 <= nx < m and 0 <= ny < n and data[ny][nx] == 1 and v[ny][nx] == 0:
                v[ny][nx] = 1
                q.append((ny,nx))
    return 0
    
    
n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

answer = bfs()
print(answer)