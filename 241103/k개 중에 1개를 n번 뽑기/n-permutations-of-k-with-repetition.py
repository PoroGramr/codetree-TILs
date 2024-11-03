from itertools import product
data = []

n,m = map(int, input().split())

combinations = product(range(1, n + 1), repeat=m)

for s in combinations:
    print(*s)