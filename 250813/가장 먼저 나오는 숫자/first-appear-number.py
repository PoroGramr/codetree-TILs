def bst(arr,target):

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


n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.

for q in query:
    result = bst(arr, q) 
    if result == len(arr) or arr[result] != q:
        print(-1)
    else:
        print(result + 1)