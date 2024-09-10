"""
문제이해
- 입력 : N, B (학생수, 예산)
        N번 반복
            P, S (선물의 가격, 배송비)

- 출력 : 선물 가능한 학생의 최대 명수

선생님이 N명의 학생에게 B만큼의 예산으로 선물을 주려고 함.
학생 i가 원하는 선물의 가격 P와 배송비 S가 있음
선생님은 선물 하나를 정해서 반값으로 할인 받을 수 있는 쿠폰이 있음.
이때, 선물 가능한 학생의 최대 명수를 구하는 프로그램을 작성

아이디어
- 각 선물을 순차대로 반값 쿠폰을 썻다고 가정하고 반복문을 돌린다?

중요 포인트
- (상품 가격 + 배송비)가 낮은 순으로 정렬시키고 완전 탐색을 진행헤야 한다는 점이 중요한 문제이다. 

"""

N,B = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int,input().split())))

# 상품 가격 + 배송비가 낮은순부터 정렬한다
data.sort(key=lambda x : (x[0] + x[1]))

answer = 0
for i in range(len(data)):
    cost = 0 # 비용 계산을 위한 변수
    chkStu = 0 # 학생수를 카운트 하기 위한 변수

    # k는 반값 쿠폰을 적용할 상품의 인덱스를 의미한다.
    # 첫번째 상품부터 차례차례 반값쿠폰을 적용하며 최대 학생 수를 계산한다.
    for k in range(len(data)):

        # 만약 반값 쿠폰을 적용해야하는 상품이라면
        if k == i:
            if cost + (data[k][0] // 2) + data[k][1] <= B:
                cost += (data[k][0] // 2) + data[k][1]
                chkStu += 1
        
        # 반값 쿠폰을 적용하지 않는 상품이라면
        else:
            if cost + data[k][0] + data[k][1] <= B:
                cost += data[k][0] + data[k][1]
                chkStu += 1
    
    # 최대 학생수 업데이트
    answer = max(answer, chkStu)

print(answer)