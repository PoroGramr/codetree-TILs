n = int(input())

data = list(map(int, input().split()))


answer = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j+1, n):
            if (i < j and j < k) and (data[i] <= data[j] and data[j] <= data[k]):
                answer += 1


print(answer)