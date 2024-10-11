n, m = map(int, input().split())
data = []
d = dict()

for i in range(n):
    data.append(input())

for j, elem in enumerate(data):
    d[elem] = j + 1

for _ in range(m):
    com = input()

    if com.isdigit():
        print(data[int(com) - 1])
    else:
        print(d[com])