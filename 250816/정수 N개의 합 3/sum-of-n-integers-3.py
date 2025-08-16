n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
[0, 0, 0, 0],
[0, 1, 2, 3],
[0, 9, 8, 8],
[0, 6, 8, 8]
"""

grid = [[0] * (n + 1) for _ in range(n + 1)]
prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        grid[i + 1][j+ 1] = arr[i][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i][j]


answer = 0
for i in range(k, n + 1):
    for j in range(k, n + 1):
        tmp = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
        answer = max(tmp, answer)

print(answer)