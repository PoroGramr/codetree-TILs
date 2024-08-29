data = [0] * 200
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    a += 100
    b += 100
    for j in range(a-1,b - 1):
        data[j] += 1


print(max(data))