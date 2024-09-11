import sys

A, B, x,y = map(int, input().split())

# 바로 가는 경우
case1 = B - A

# x를 들렸다가 가는 경우
case2 = abs(A - x) + abs(B - y)

# y를 들렸다가 가는 경우
case3 = abs(y - A) +abs(B - x)

answer = min(case1, case2, case3)

print(answer)