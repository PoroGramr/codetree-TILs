import heapq

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

heap = []
for point in points:
    x = point[0]
    y = point[1]
    heapq.heappush(heap, ((x+y), x, y))

for _ in range(m):
    curSum,x,y = heapq.heappop(heap)
    x += 2
    y += 2
    heapq.heappush(heap, ((x+y), x, y))

_curSum, x, y = heapq.heappop(heap)
print(x, y)