X, Y = map(int, input().split())

answer = 0
for i in range(X, Y+1):
    i = str(i)
    rev = i[::-1]
    if i == rev:
        answer += 1


print(answer)