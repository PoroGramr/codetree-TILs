n = int(input())
data = list(map(int,input().split()))

dataup = sorted(data)
datadown = dataup[::-1]


for i in dataup:
    print(i, end =" ")
print()
for i in datadown:
    print(i, end =" ")