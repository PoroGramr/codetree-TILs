a , b = map(int, input().split())

n = int(input())

nData = list(map(int, str(n)))


num1 = 0
for i in range(len(nData)):
    num1 = num1 * a + nData[i]

answer = []

while True:
    if num1 < b:
        answer.append(num1)
        break
    answer.append(num1 % b)
    num1 = num1 // b

for i in answer[::-1]:
    print(i, end = "")