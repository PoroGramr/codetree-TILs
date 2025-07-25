n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

pick = []



answer = 0

def check(curNum):
    if curNum == n + 1:
        calc()
        return
    
    for i in range(1,k + 1):
        pick.append(i)
        check(curNum + 1)
        pick.pop()
    
def calc():
    global answer
    tmpAnswer = 0
    position = [0] * k

    for j in range(len(pick)):
        x = pick[j] - 1
        position[x] += nums[j]
    
    for point in position:
        if point >= n - 1:
            tmpAnswer += 1
    answer = max(tmpAnswer, answer)


check(1)
print(answer-1)