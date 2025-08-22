n = int(input())
arr = list(map(int, input().split()))

NEG = -10**9                 # 도달 불가 표시
dp = [NEG] * n
dp[0] = 0                    # 시작점: 점프 0번으로 도달

for i in range(1, n):        # i는 도착 지점
    for j in range(i):       # j는 직전 위치
        if dp[j] == NEG:     # j 자체가 도달 불가면 스킵
            continue
        if j + arr[j] >= i:  # j에서 i로 점프 가능?
            dp[i] = max(dp[i], dp[j] + 1)

ans = max(dp)
print(1 if ans < 0 else ans) # 전혀 못 움직이면 0