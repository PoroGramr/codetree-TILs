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
        
        if len(nums) >= 2:
            if nums[num-2] == nums[num-3] and nums[num-2] == i:
                continue
        nums.append(i)
        choose(num + 1)
        nums.pop()
    
choose(1)
