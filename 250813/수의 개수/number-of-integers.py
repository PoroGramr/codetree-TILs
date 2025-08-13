# bst 로 탐색 후 개수 리턴
def minBst(arr, target):
    left = 0
    right = len(arr) - 1

    minIdx = len(arr)

    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] >= target:
            minIdx = min(minIdx, mid)
            right = mid - 1
        
        else:
            left = mid + 1
        
    
    return minIdx

def maxBst(arr, target):
    left = 0
    right = len(arr) - 1
    
    maxIdx = -1

    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] <= target:
            maxIdx = max(maxIdx, mid)
            left = mid + 1
        
        else:
            right = mid - 1
        
    
    return maxIdx



n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

# for문으로 쿼리 함수에 삽입

for query in queries:
    minIdx = minBst(arr, query)
    maxIdx = maxBst(arr, query)
    print(maxIdx - minIdx + 1)
