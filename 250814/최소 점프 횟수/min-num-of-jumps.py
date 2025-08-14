n = int(input())
num = list(map(int, input().split()))

answer = float('inf')

def dfs(pos, depth):
    global answer

    if pos == n - 1:
        answer = min(answer, depth)
        return

    if depth >= answer:
        return

    max_jump = num[pos]
    for step in range(1, max_jump + 1):
        next_pos = pos + step
        if next_pos < n:
            dfs(next_pos, depth + 1)

dfs(0, 0)

print(answer if answer != float('inf') else -1)