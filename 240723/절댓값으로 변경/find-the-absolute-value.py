def abso(n):
    data = list(map(int, input().split()))
    for i in data:
        print(abs(i), end = " ")


n = int(input())
abso(n)