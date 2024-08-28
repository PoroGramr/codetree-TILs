def check(a,b,c):
    if a < 11:
        return "-1"
    if a == 11 and b <= 11 and c <= 11:
        return "-1"
    
    dayMin = a * 24 * 60
    hourMin = b * 60
    totalMin = dayMin + hourMin + c

    pinMin = (11 * 24 * 60) + (11 * 60) + 11

    answer = totalMin - pinMin

    return answer




a, b, c = map(int, input().split())
print(check(a,b,c))