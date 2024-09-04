import sys

data = list(map(int, input().split()))

max = -sys.maxsize

for i in data:
    if i > max:
        max = i

print(max)