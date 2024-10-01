a,b = map(int, input().split())

n = str(input())

# a진수 n을 10진수로 변환
data = list(n)
data.reverse()
num = 0
for k in range(len(data)):
    if k == 0:
        num += int(data[k])
    else:
        num += (a ** k) * int(data[k])
# 10진수로 변환한 n을 b진수로 변환
answerNum = []
while num != 0:
    answerNum.append(str(num % b))
    num //= b
# 역순으로 저장되어있기에 리버스 해준다
answerNum.reverse()

# 리스트를 문자열로 변환
answer =""
for a in answerNum:
    answer = answer + str(a)

print(answer)