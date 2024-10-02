def dfs(y, x, M, N):
    if y == (M - 1) and x == (N - 1):
        return 1

    for py, px in ((0, 1), (1, 0)):
        ny, nx = y + py, x + px
        if 0 <= ny < M and 0 <= nx < N and data[ny][nx] == 1 and v[ny][nx] == 0:
            v[ny][nx] = 1
            if dfs(ny, nx, M, N) == 1:  # 탈출 경로를 찾으면 1 반환
                return 1
            v[ny][nx] = 0  # 경로를 찾지 못한 경우 방문 처리 해제

    return 0

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]
v[0][0] = 1  # 시작 지점을 방문 처리
answer = dfs(0, 0, N, M)
print(answer)