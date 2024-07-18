def onjunsu(a,b):
    sum = 0
    for i in range(a,b+1):
        if i % 2 != 0 and (i % 10) != 5 and not(i % 3 == 0 and i % 9 != 0):
            sum += 1
    return sum


a ,b = map(int, input().split())
answer = onjunsu(a,b)
print(answer)