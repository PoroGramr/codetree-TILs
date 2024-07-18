'''
1. Y,M,D에 연도 월 일을 차례로 입력받는다.
2. checkDay(Y,M,D)를 통해 존재하는 날인지 체크한다.
2-1. 윤년일때의 각 월 날 배열 [31,29,31,30,31...] 과 
일반 월 날 배열 [31,28,31,30...] 을 선언 및 정의한다.
2-2. 해당 년도가 윤년인지 체크한다.
2-3. 해당 날짜가 존재하는 날짜인지 체크한다.
3. 존재하는 날짜라면 checkWhether을 통해 계절을 리턴한다.
4. 위 과정을 진행하는 중 한번이라도 False가 난다면 -1을 리턴한다.
'''
def checkDay(y,m,d):
    yoonDays = [31,29,31,30,31,30,31,31,30,31,30,31]
    basicDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if checkYoonYear(y):
        if yoonDays[m-1] >= d:
            return True
        else:
            return False
    else:
        if basicDays[m-1] >= d:
            return True
        else:
            return False
    

def checkYoonYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            return False
        return True
    return False

def checkWhether(M):
    if M >= 3 and M <= 5:
        return "Spring"
    elif M >= 6 and M <= 8:
        return "Summer"
    elif M <= 9 and M >= 11:
        return "Fall"
    else:
        return"Winter"


Y,M,D = map(int,input().split())
answer = ""
if checkDay(Y,M,D):
    answer = checkWhether(M)
else:
    answer = -1
print(answer)