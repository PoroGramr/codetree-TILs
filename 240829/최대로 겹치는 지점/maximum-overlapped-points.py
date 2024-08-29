data = [0] * 100

n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    for k in range(a-1,b):
        data[k] += 1

print(max(data))