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
answerNum = []
while num != 0:
    answerNum.append(str(num % b))
    num //= b
answerNum.reverse()
answer =""
for a in answerNum:
    answer = answer + str(a)

print(answer)