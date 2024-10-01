data = list(input())
count = 0
for i in range(len(data)):
    if data[i] == "(":
        for k in range(i, len(data)):
            if data[k] == ")":
                count += 1
print(count)