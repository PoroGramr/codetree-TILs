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

"""

N,B = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x : (x[0] + x[1]))

answer = 0
for i in range(len(data)):
    cost = 0
    chkStu = 0
    for k in range(len(data)):
        if k == i:
            if cost + (data[k][0] // 2) + data[k][1] <= B:
                cost += (data[k][0] // 2) + data[k][1]
                chkStu += 1
        else:
            if cost + data[k][0] + data[k][1] <= B:
                cost += data[k][0] + data[k][1]
                chkStu += 1
    answer = max(answer, chkStu)

print(answer)