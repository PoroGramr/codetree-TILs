import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
missing = [0] * (N + 1)

for _ in range(B):
    x = int(input())
    missing[x] = 1

# 누적합 배열
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + missing[i]

# 연속된 K개 구간 중 최소 빠진 숫자 개수
ans = K
for i in range(1, N - K + 2):
    j = i + K - 1
    missing_count = prefix[j] - prefix[i-1]
    ans = min(ans, missing_count)

print(ans)