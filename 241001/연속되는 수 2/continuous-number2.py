k = int(input())
data = []
for _ in range(k):
    data.append(int(input()))
count = 0
answer = 0
for i in range(k):
    if i == 0 or data[i-1] == data[i]:
        count += 1
    else:
        count = 1
    answer = max(answer,count)
print(answer)