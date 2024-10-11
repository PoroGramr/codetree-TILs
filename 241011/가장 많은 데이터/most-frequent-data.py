n = int(input())

d = dict()

for _ in range(n):
    com = str(input())

    if com in d:
        d[com] += 1
    else:
        d[com] = 1
print(max(d.values()))