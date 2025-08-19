import math

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = []
arr2 = []
answer = 9999999

def choose2(curNum, start):
    global answer
    if curNum == 3:
        tmp = (arr2[0][0] - arr2[1][0])**2 + (arr2[0][1] - arr2[1][1])**2
        answer = min(answer, tmp)
        return

    for i in range(start, len(arr)):
        arr2.append(arr[i])
        choose2(curNum + 1, i + 1)   
        arr2.pop()                   

def choose(curNum, start):
    if curNum == m + 1:
        choose2(1, 0)
        return

    for i in range(start, n):
        arr.append(points[i])
        choose(curNum + 1, i + 1)
        arr.pop()

choose(1, 0)
print(answer)