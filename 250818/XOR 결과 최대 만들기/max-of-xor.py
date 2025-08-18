n, m = map(int, input().split())
A = list(map(int, input().split()))

answer = 0

def dfs(start, depth, xo):
    # m개를 다 골랐으면 갱신
    if depth == m:
        global answer
        if xo > answer:
            answer = xo
        return

    # 남은 칸으로 m-depth개를 못 채우면 가지치기
    # (선택 가능한 시작 인덱스 최댓값은 n - (m - depth))
    for i in range(start, n - (m - depth) + 1):
        dfs(i + 1, depth + 1, xo ^ A[i])

dfs(0, 0, 0)
print(answer)
