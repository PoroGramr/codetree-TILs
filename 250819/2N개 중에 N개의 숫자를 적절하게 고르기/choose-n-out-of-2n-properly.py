n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
arr1 =[]
arr2 = []

answer = sum(num)
numSum = sum(num)
def choose(curNum,start):
    global answer, numSum
    if curNum == n + 1:
        tmp = sum(arr1)
        rest = numSum - tmp

        bet = abs(tmp - rest)
        answer = min(answer, bet)
        return
    
    for i in range(start,2*n):
        arr1.append(num[i])
        choose(curNum + 1, i + 1)
        arr1.pop()


choose(1,0)

print(answer)