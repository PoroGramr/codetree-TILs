N, M = map(int, input().split())

arr = []

def dfs(start, depth):
    if depth == M:
        print(*arr)
        return
    # 다음 수는 반드시 start 이상 → 자동으로 오름차순, 중복X
    for i in range(start, N + 1):
        arr.append(i)
        dfs(i + 1, depth + 1)
        arr.pop()

dfs(1, 0)