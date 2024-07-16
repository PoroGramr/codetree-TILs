def all_sum(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    sum = sum // 10 
    print(sum)
k = int(input())
all_sum(k)