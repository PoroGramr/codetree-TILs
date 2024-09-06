"""
for 문을 돌리며 입력 문자를 완전 탐색
만약 "(" 를 만난다면 
    만난 시점 이후부터 ")"의 개수를 확인
    answer += 1

"""

inStr = input()

strData = list(inStr)

answer = 0

for i in range(len(strData)):
    if strData[i] == "(":
        for k in range(i, len(strData)):
            if strData[k] == ")":
                answer += 1


print(answer)