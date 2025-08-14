n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# K개(1 ~ K)를 n번 골라야 함(중복 가능)

# 선택된 말들을 바탕으로 점수 최대값 계산

maxScore = 0

data = []

def calcMax(pins):
    global maxScore
    tmpCount = 0
    x = [1] * k

    for i in range(n):
        x[pins[i]] += nums[i]
    
    for j in x:
        if j >= m:
            tmpCount += 1
    
    maxScore = max(tmpCount,maxScore)


def choose(curNum):
    if curNum == n + 1:
        calcMax(data)
        return

    for i in range(1, k):
        data.append(i)
        choose(curNum + 1)
        data.pop()



choose(1)
print(maxScore)

