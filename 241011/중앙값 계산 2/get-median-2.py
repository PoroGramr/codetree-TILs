n = int(input())
data=[]

data = list(map(int, input().split()))
for i in range(n):
    inData = data[0:i+1]
    inData.sort()
    if i % 2 == 0:
        print(inData[i // 2], end= " ")