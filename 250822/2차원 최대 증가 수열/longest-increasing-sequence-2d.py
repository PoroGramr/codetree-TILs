n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        for a in range(i + 1,n):
            for b in range(j + 1,m):
                if grid[a][b] > grid[i][j] and grid[a][b] > grid[0][0]:
                    dp[a][b] = max(dp[a][b] ,dp[i][j] + 1)

answer = 0
for y in range(n):
    for x in range(m):
        answer = max(dp[y][x], answer)

print(answer)