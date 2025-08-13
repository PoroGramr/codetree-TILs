import bisect

N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    s, e = map(int, input().split())
    left = bisect.bisect_left(points, s)   
    right = bisect.bisect_right(points, e) 
    print(right - left)
