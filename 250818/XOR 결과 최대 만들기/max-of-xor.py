

n, m = map(int, input().split())
A = list(map(int, input().split()))

answer = 0

arr = []
def dfs(curNum, start):
    global answer
    if curNum == m + 1:
        res = 0
        for a in arr:
            res ^= a
        if res > answer:
            answer = res
        return

    for i in range(start, n + 1):
        arr.append(A[i - 1])    # 값 추가 (인덱스 X)
        dfs(curNum + 1, i + 1)  # 다음 시작은 i+1 (조합)
        arr.pop()

dfs(1, 1)
print(answer)
