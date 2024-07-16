'''
1. a,b를 입력 받는다.
2. for문을 통해 a,b사이에 모든 요소를 접근
3. 접근한 요소(n)를 for문을 통해 2 ~ n 까지 접근하며 소수인지 판단
3-1. 소수일경우 결과값에 더함
3-2. 소수가 아닐경우 아무 행위 하지 않음
4. 결과값 리턴
'''
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def checkPrime(a,b):
    sum = 0
    for i in range(a,b+1):
        if isPrime(i):
            sum += i
    return sum

a ,b = map(int, input().split())
answer = checkPrime(a,b)
print(answer)