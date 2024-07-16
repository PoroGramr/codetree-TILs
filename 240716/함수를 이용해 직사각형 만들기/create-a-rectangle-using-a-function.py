def print_rect(n,m):
    for _ in range(n):
        print("1" * m)

a,b = map(int, input().split())
print_rect(a,b)