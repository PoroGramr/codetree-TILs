n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
countDict = {}

for num in arr:
    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1

for count in nums:
    if count in countDict:
        print(countDict[count], end =" ")
    else:
        print("0", end =" ")