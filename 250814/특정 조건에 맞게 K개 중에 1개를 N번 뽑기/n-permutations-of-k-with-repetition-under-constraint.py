K, N = map(int, input().split())

# Please write your code here.
nums = []
def choose(num):
    if num == N + 1:
        for n in nums:
            print(n, end=" ")
        print()
        return

    for i in range(1, K + 1):
        lenNums = len(nums)

        if lenNums >= 2:
            if nums[lenNums-2] == nums[lenNums-1] and nums[lenNums-1] == i:
                continue

        nums.append(i)
        choose(num + 1)
        nums.pop()
    
choose(1)
