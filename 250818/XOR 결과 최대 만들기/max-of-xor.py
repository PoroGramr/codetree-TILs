n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

answer = 0


arr = []
def dfs(curNum,start):
    global answer 
    if start == m + 1:
        res = 0
        for a in arr:
            res ^= a

        answer = max(res,answer)
        return


    for i in range(start, n + 1):
        arr.append(i)
        dfs(curNum + 1, start + 1)
        arr.pop()


dfs(1, 1)
print(answer)