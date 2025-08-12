import heapq

n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
h = []

for check in x:
    if check == 0:
        if h:
            minNum = heapq.heappop(h)
            print(minNum)
        else:
            print(0)
    else:
        heapq.heappush(h,check)
