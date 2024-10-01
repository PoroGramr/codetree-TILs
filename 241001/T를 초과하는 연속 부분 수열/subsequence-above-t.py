n, t = map(int, input().split())

data = list(map(int, input().split()))

count = 0
answer = 0
for i in range(n):
    if n == 0 or data[i-1] > t and data[i] > t:
        count += 1
    else:
        count = 1
    answer = max(answer, count)
print(answer)