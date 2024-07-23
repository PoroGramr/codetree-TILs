def check(a,b):
    if a > b:
        print(a * 2, end =" ")
        print(b + 10)
    else:
        print(a + 10, end = " ")
        print(b * 2)

a,b = int(input())
check(a,b)