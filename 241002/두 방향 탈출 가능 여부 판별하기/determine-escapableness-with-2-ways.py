def dfs(y, x, M, N):
    # 목적지에 도착한 경우
    if y == (M - 1) and x == (N - 1):
        return True

    # 오른쪽, 아래 방향으로만 이동
    for py, px in ((0, 1), (1, 0)):
        ny, nx = y + py, x + px
        # 이동 가능한 범위 내, 이동 가능한 칸(1), 아직 방문하지 않은 경우
        if 0 <= ny < M and 0 <= nx < N and data[ny][nx] == 1 and v[ny][nx] == 0:
            v[ny][nx] = 1  # 방문 처리
            if dfs(ny, nx, M, N):  # 경로를 찾으면 즉시 True 반환
                return True

    return False

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]

# 탈출 가능한 경로가 있으면 1, 없으면 0 출력
if dfs(0, 0, N, M):
    print(1)
else:
    print(0)