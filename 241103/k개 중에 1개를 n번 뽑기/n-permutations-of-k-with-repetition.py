from itertools import product
data = []

n,m = map(int, input().split())

combinations = product(range(1, m + 1), repeat=n)

for s in combinations:
    print(*s)