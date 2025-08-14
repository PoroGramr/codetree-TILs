import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    a = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0]*n for _ in range(n)]
    dp[0][0] = a[0][0]

    # 첫 행
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], a[0][j])

    # 첫 열
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], a[i][0])

    # 나머지 칸
    for i in range(1, n):
        for j in range(1, n):
            from_top = max(dp[i-1][j], a[i][j])
            from_left = max(dp[i][j-1], a[i][j])
            dp[i][j] = min(from_top, from_left)

    print(dp[n-1][n-1])

if __name__ == "__main__":
    solve()