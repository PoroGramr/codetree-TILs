def lower(arr, target):
    left = 0
    right = len(arr) - 1
    idx = len(arr)

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] >= target:
            idx = min(idx, mid)
            right = mid - 1
        else:
            left = mid + 1      
    return idx  

def upper(arr, target):
    left = 0
    right = len(arr) - 1
    idx = -1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] <= target:
            idx = max(idx, mid)
            left = mid + 1
        else:
            right = mid - 1
    
    return idx


N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    s, e = map(int, input().split())
    a = lower(points,s)
    b = upper(points,e)
    print(b-a + 1)
