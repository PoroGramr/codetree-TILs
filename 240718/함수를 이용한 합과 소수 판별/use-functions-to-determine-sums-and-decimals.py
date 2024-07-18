'''
1. 정수 a,b를 입력받는다.
2. 소수이면서 자릿수의 합이 짝수인 수의 개수를 구하는 함수 정의

'''
def prime(a):
    for i in range(2,a):
        if (a % i == 0):
            return False
    return True

def even(a):
    numlist = list(map(int, str(a)))
    sumnum = sum(numlist)
    if sumnum % 2 == 0:
        return True
    else:
        return False


def determine(a,b):
    sum = 0
    for i in range(a,b+1):
        if prime(i) and even(i):
            sum += 1
    return sum

a,b = map(int, input().split())
answer = determine(a,b)
print(answer)