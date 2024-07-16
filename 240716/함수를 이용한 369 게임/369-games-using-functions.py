'''
1. a,b를 입력 받는다.
2. for 문을 통해 a,b 모든 요소를 접근한다.
3. 3,6,9 중 하나가 있는 지 체크
3-1. 숫자를 문자 1씩으로 쪼개 3, 6, 9 인지 체크
4. 3의 배수인지 체크
4-1. if %3 == 0 으로 3의 배수인지 체크 
'''
def check369(n):
    strnum = str(n)
    if "3" in strnum:
        return True
    elif "6" in strnum:
        return True
    elif "9" in strnum:
        return True
    
    return False
        

def check3x(n):
    if n % 3 == 0:
        return True
    return False

def func369(a,b):
    sum = 0 
    for i in range(a, b+1):
        if check369(i):
            sum += 1
            continue
        elif check3x(i):
            sum += 1
            continue
    return sum

num1, num2 = map(int, input().split())
answer = func369(num1, num2)
print(answer)