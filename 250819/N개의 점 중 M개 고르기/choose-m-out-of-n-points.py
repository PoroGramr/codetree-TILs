import math

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

arr = []
arr2 = []
answer = float('inf')   # 최솟값 갱신용
currentMax = 0          # 선택된 M개 집합 내 최댓 제곱거리

def choose2(curNum, start):
    # arr(길이 m)에서 2개 뽑아 최댓 제곱거리 계산
    global currentMax
    if curNum == 3:  # 2개 뽑으면 종료
        # 유클리드 거리의 제곱(√ 생략)
        tmp = (arr2[0][0] - arr2[1][0])**2 + (arr2[0][1] - arr2[1][1])**2
        currentMax = max(currentMax, tmp)   # 집합 내 최댓값 갱신
        return
    for i in range(start, len(arr)):
        arr2.append(arr[i])
        choose2(curNum + 1, i + 1)   # (함수명/진행 인덱스 유지)
        arr2.pop()                   # ← arr2에서 팝

def choose(curNum, start):
    global answer, currentMax
    if curNum == m + 1:
        currentMax = 0          # 새 집합마다 리셋
        choose2(1, 0)           # arr에서 2개 조합 전부 확인
        answer = min(answer, currentMax)  # 최댓값의 최소화
        return
    for i in range(start, n):
        arr.append(points[i])
        choose(curNum + 1, i + 1)
        arr.pop()

choose(1, 0)
print(answer)