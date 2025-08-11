n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = grid[0][0]

for i in range(1,n):
    for j in range(n):
        if j == 0 and i == 0:
            continue

        if j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = max(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])


# for j in range(n):
#     for i in range(n):
#         print(dp[j][i], end=" ")
#     print()        


print(dp[n-1][n-1])

