def dfs(y,x,M,N):

    if y == (M - 1) and x == (N - 1):
        return 1

    for py,px in ((0,1),(1,0)):
        ny ,nx = y + py, x + px
        if 0 <= ny < M and 0 <= nx <N and v[ny][nx] == 0:
            v[ny][nx] = 1
            if dfs(ny, nx, M, N) == 1:  # 탈출 경로를 찾으면 1 반환
                return 1
    return 0


N,M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
v = [[0 for _ in range(N)] for _ in range(M)]
answer = dfs(0,0,N,M)
print(answer)