N = int(input())
# 1,2,3층
dp = [0,1,1]

for i in range(3, N + 1):
    dp.append(0)
    dp[i] = dp[i-2] + dp[i-3]

print(dp[N-1] % 10007)