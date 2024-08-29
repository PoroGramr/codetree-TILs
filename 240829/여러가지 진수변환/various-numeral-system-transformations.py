num, n = map(int, input().split())

answer = []

while True:
    if num < n:
        answer.append(num)
        break
    
    answer.append(num % n)
    num = num // n

for ans in answer[::-1]:
    print(ans, end="")