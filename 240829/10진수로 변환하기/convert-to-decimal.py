num = input()
data = list(map(int, num))

answer = 0
for i in range(len(data)):
    answer = answer * 2 + data[i]
print(answer)