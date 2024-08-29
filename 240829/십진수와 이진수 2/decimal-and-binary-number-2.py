num = input()

data = list(map(int, num))

answer = 0
for i in range(len(data)):
    answer = answer * 2 + data[i]

answer = answer * 17

binary = []

while True:
    if answer < 2:
        binary.append(answer)
        break
    binary.append(answer % 2)
    answer = answer // 2


for i in binary[::-1]:
    print(i, end="")