n = int(input())
data = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if i<j<k and data[i]<= data[j] <= data[k]:
                count += 1

print(count)