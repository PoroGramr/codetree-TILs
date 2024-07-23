a,b = map(int, input().split())

data = list(map(int, input().split()))
answer = 0
while(b > 0):
    if b % 2 == 0:
        answer += data[b-1]
        b //= 2
    else:
        answer += data[b-1]
        b -= 1

print(answer)