def down(n):
    if n == 0:
        return
    print(n,end = " ")
    down(n-1)

def up(n):
    if n == 0:
        return
    up(n-1)
    print(n, end = " ")

n = int(input())

up(n)
print()
down(n)