N ,K = map(int, input().split())

data = [0] * N

for i in range(K):
    a,b = map(int, input().split())
    for j in range(a,b+1):
        data[j] +=1

    
print(max(data))