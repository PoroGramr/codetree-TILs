from itertools import combinations
data = []

n,m = map(int, input().split())

for s in combinations(n,m):
    data.append(s)

print(len(data))