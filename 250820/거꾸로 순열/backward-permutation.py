n = int(input())

arr = []
used = [False] * (n + 1)

def dfs(depth):
    if depth == n:
        print(*arr)
        return
    
    for x in range(n, 0, -1):  # 매 단계에서 n→1 순서
        if not used[x]:
            used[x] = True
            arr.append(x)
            dfs(depth + 1)
            arr.pop()
            used[x] = False

dfs(0)