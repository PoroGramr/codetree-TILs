import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

h = []

for num in arr:
    heapq.heappush(h, -num)

for _ in  range(m):
    num = -heapq.heappop(h)
    num -= 1
    heapq.heappush(h,-num)

maxNum = -heapq.heappop(h)

print(maxNum)