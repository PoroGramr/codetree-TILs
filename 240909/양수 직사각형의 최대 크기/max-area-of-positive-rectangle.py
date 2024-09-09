"""
문제이해
- 입력
    n,m : 이차원 영역의 크기(가로, 세로)
    리스트 : 2차원 영역에 들어간 정수들의 리스트

- 출력
    정수 : 모든값이 양수로만 이루어져 있는 직사각형 중 최대 크기를 출력(가로 * 세로)

아이디어
- 입력으로 받은 n,m을 바탕으로 만들수 있는 모든 직사각형의 크기를 계산하며 
전체 탐색을 해야함
1. 직사각형의 가로 세로를 지정
2. 지정한 가로, 세로 길이를 바탕으로 모든 가능한 직사각형을 탐색
    2-1. 만약 지정한 직사각형 모든 요소가 정수라면
        2-1-1. 넓이를 계산해 answer에 저장
3. answer를 출력

"""

n,m = map(int, input().split())

data = []

for i in range(n):
    x = list(map(int, input().split()))
    data.append(x)

answer = -1

conCheck = 0

for i in range(n): # 세로 길이 1부터 시작 
    for k in range(m): # 가로 길이 1부터 시작 # 즉, 직사각형의 크기는 n*m(1*1, 1*2....2*1, 2*2, 2*3,...n*m)
        for a in range(0,n - i): # 시작점 y
            for b in range(0,m - k): # 시작점 x
                conCheck = 0
                for ax in range (a, a + i + 1): # y값 a ~ a + i 를 탐색
                    for bx in range(b, b + k + 1): # x값 b ~ b + k를 탐색
                        if data[ax][bx] <= 0: # 만약 음수가 있다면
                            conCheck = 1 # for문 2개를 한번에 멈추는 건 불가능 하기에 변수로 2개를 멈춤
                            break
    
                if conCheck == 0:
                    # print(a,b, end ="")
                    # print("부터",a+i, b+k, "까지")
                    # print(i + 1, " *", k + 1)
                    
                    # 최대값을 지속해서 업데이트
                    answer = max(answer , (i + 1) * (k+1))      
                    

                # print(a,b, end ="")
                # print("부터",a+i, b+k, "까지")

print(answer)