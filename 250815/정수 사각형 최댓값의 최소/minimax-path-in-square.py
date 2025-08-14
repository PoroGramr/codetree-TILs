n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]


dp[0][0] = grid[0][0]
for i in range(1,n):
    dp[0][i] = max(grid[0][i], dp[0][i-1])

for i in range(1,n):
    dp[i][0] = max(grid[i][0], dp[i-1][0])

for y in range(1,n):
    for x in range(1,n):
        top = max(grid[y][x], dp[y-1][x])
        left = max(grid[y][x], dp[y][x-1])
        minValue = min(top,left)
        dp[y][x] = minValue


print(dp[n-1][n-1])