n = int(input())
data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append([a,b])

# 1 가위 2 바위 3 보
count1 = 0
for a,b in data:
    if a == 1 and b == 3:
        count1 += 1
    elif a == 2 and b == 1:
        count1 += 1
    elif a == 3 and b == 2:
        count1 += 1

# 1 가위 2 보 3 바위
count2 = 0
for a,b in data:
    if a == 1 and b == 2:
        count2 += 1
    elif a == 2 and b == 3:
        count2 += 1
    elif a == 3 and b == 1:
        count2 += 1

ans = max(count1, count2)

print(ans)