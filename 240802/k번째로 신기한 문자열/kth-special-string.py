n, k , start = input().split()
data = []
for _ in range(int(n)):
    data.append(input())

answerData = []
for _data in data:
    if _data[0:len(start)] == start:
        answerData.append(_data)
print(answerData)