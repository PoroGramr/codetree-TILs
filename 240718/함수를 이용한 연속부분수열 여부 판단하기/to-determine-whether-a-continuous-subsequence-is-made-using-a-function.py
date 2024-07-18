'''
1. 2개 배열의 길이를 입력 받는다
2. 배열을 입력 받는다.
3. 배열 A 의 모든 연속 부분 수열을 생성한다.그후 배열 C에 append
4. 배열C에 배열 B가 존재 하는 지 확인
'''

def makelist(sequence):
    subsequences = []
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence) + 1):
            subsequences.append(sequence[i:j])
    return subsequences

            


alen, blen = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


c = makelist(a)
if b in c:
    print("Yes")
else:
    print("No")