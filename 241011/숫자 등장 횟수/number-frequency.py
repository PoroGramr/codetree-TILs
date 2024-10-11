n, m = map(int, input().split())

d = dict()
data= list(map(int, input().split()))
com = list(map(int, input().split()))
for i in range(n):
    if not data[i] in d:
        d[data[i]] = 1
    else:
        d[data[i]] += 1
for j in range(m):
    if com[j] in d:
        print(d[com[j]], end = " ")
    else:
        print(0, end=" ")