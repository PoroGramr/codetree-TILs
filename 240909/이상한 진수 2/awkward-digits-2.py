num = input()

numList = list(num)

# 첫번쨰 for문을 거치는지 안거치는 지 확인을 위한 변수
changeCount  = 0

# 만약 0이 있다면 1로 바꾸고 for문 탈출
for i in range(len(numList)):
    if numList[i] == '0':
        numList[i] = '1'
        changeCount = 1
        break

# 0이 없다면 1을 0으로 바꾸고 for문 탈출
# 위 for문을 통과하고 변화가 없다면 실행됨
if changeCount == 0:
    for i in range(len(numList) - 1,0,-1):
        if numList[i] == '1':
            numList[i] = '0'
            break

# 리스트의 요소를 하나의 문자로 결합
answer = "".join(numList)

# 2진수를 10진수로 변환
answer = int(answer, 2)

print(answer)