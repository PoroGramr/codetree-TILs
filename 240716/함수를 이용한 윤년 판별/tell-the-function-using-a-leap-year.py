def checkYoonYear(n):
    if n % 100 == 0 and n % 400 != 0:
        return "false"
    elif n % 4 == 0:
        return "true"
    return "false"

n = int(input())
answer = checkYoonYear(n)
print(answer)