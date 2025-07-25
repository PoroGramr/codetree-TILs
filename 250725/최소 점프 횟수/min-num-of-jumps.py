n = int(input())
num = list(map(int, input().split()))

answer = 99999

def check(curNum, lens):
    if curNum == lens + 1:
        calc()
        return
    
    for k in range(1, n-1):
        tmpMax = max(nums)
        if k > tmpMax:
            nums.append(k)
            check(curNum + 1, lens)
            nums.pop()

def calc():
    global answer

    for j in range(1,len(nums)):
        if nums[j-1] + num[j - 1] >= nums[j]:
            continue
        else:
            return
    if nums[-1] + num[nums[-1]] >= n - 1:
        answer = min(answer, len(nums))

for i in range(1, n + 1):
    nums = [0]

    check(1, i)

if answer == 99999:
    answer = -1
print(answer)



