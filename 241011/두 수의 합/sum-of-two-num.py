import sys

# 재귀 깊이 제한 해제 또는 증가 (예: 10,000으로 설정)
sys.setrecursionlimit(100000)


def dfs(i, res):
    global ans

    if i == n:
        if res == k:
            ans += 1
        return
    
    dfs(i+1, res + data[i])

    dfs(i+1, res)
    


n, k = map(int, input().split())

data = list(map(int, input().split()))
ans = 0
dfs(0,0)
print(ans)