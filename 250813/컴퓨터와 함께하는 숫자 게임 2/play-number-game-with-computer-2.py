def bs(m, target):
    left = 1
    right = m

    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        if mid == target:          
            return cnt

        if mid > target:
            right = mid - 1
            
        else:
            left = mid + 1

    return cnt
m = int(input())
a, b = map(int, input().split())

# Please write your code here.
minNum = m
maxNum = -1
for num in range(a, b + 1):
    count = bs(m,num)
    minNum = min(minNum, count)
    maxNum = max(maxNum, count)

print(minNum, maxNum)
