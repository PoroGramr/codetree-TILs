def f(sumData):
    if sumData < 10:
        return (sumData % 10)
    return f(sumData//10) + (sumData % 10)

a,b,c = map(int, input().split())
sumData = a * b * c
print(f(sumData))