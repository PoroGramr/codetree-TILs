def f(n):
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)



def odd(n):
    if n == 1:
        return 1
    return odd(n-2) + n

def even(n):
    if n == 2:
        return 2
    return even(n-2) + n


n = int(input())
print(f(n))