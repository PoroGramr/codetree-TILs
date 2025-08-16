n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
prefix = [0] * (n + 1)


for i in range(1, n + 1):
    prefix[i] = arr[i-1] + prefix[i-1]

# 구간 합의 길이
cnt = 0

for c in arr:
    if c == k:
        cnt += 1

for l in range(1, n + 1):
    # print(l)
    for a in range(1,n - l + 1):
        tmp = prefix[a +l] - prefix[a - 1]
        if tmp == k:
            cnt += 1
        # print(a, a + l)

print(cnt)