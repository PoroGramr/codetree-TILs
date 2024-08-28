def check(a,b,c):

    # 예외 입력 리턴
    if a < 11:
        return "-1"
    if a == 11 and b < 11:
        return "-1"
    
    
    # 입력된 날짜의 분의 합을 계산(기준은 11월 1일 00시 00분)
    dayMin = a * 24 * 60    # 일자를 기준으로 분 계산
    hourMin = b * 60        # 시간을 기준으로 분 계산
    totalMin = dayMin + hourMin + c     # 총합

    pinMin = (11 * 24 * 60) + (11 * 60) + 11 # 11월 11일 11시 11분이 11월 1일 0시 00분으로 부터 얼마나 흘렀는지 분을 계산

    answer = totalMin - pinMin # 두 분 총합의 차를 리턴

    return answer




a, b, c = map(int, input().split())
print(check(a,b,c))