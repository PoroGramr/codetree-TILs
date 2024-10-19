from collections import deque

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))

    while q:
        cy, cx = q.popleft()

        # 도착점에 도달하면 현재 이동 횟수를 반환
        if cy == r2 - 1 and cx == c2 - 1:
            return data[cy][cx]
        
        # 나이트의 8가지 이동 방향
        for dy, dx in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            ny, nx = cy + dy, cx + dx
            
            # 유효한 범위인지 확인하고, 방문하지 않았던 위치인지 확인
            if 0 <= ny < n and 0 <= nx < n and data[ny][nx] == -1:
                # 거리 업데이트
                data[ny][nx] = data[cy][cx] + 1
                q.append((ny, nx))

    return -1  # 도달할 수 없는 경우

n = int(input())

r1, c1, r2, c2 = map(int, input().split())
data = [[-1] * n for _ in range(n)]
data[r1 - 1][c1 - 1] = 0  # 시작 위치에서의 거리 초기화

ans = bfs(r1 - 1, c1 - 1)

print(ans)