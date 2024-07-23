def check_unique_alphabets(A):
    # 문자열 A에서 서로 다른 알파벳의 집합을 구합니다.
    unique_alphabets = set(A)
    
    # 집합의 크기가 2개 이상이면 Yes, 아니면 No를 출력합니다.
    if len(unique_alphabets) >= 2:
        return "Yes"
    else:
        return "No"

# 사용자로부터 문자열 입력을 받습니다.
inputString = input()
print(check_unique_alphabets(inputString))