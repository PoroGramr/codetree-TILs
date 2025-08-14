n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][n-1] = grid[0][n-1]

for i in range(n-2,-1,-1):
    dp[0][i] = grid[0][i] + dp[0][i+1]

for y in range(1,n):
    for x in range(n-1,-1,-1):
        if x == n-1:
            dp[y][x] = grid[y][x] + dp[y-1][x]

        else:
            dp[y][x] = grid[y][x] + min(dp[y-1][x], dp[y][x+1])
        

print(dp[n-1][0])