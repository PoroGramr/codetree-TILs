def check(a,b):
    data = [a,b]
    data.sort()
    data[0] = data[0] * 2
    data[1] = data[1] + 25

    print(data[0], end=" ")
    print(data[1])

a,b = map(int,input().split())
check(a,b)