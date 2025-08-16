n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

preSum = [0] * n

preSum[0] = arr[0]
for i in range(1, n):
    preSum[i] = arr[i] + preSum[i-1]


answer = preSum[k-1]

for j in range(k, n):
    tmp = preSum[j] - preSum[j-k]
    answer = max(tmp,answer)

print(answer)