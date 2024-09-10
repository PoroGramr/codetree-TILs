"""
문제 이해
- 입력 :
    n,m : 정수,이동횟수
    list : n개의 1~ n 까지의 리스트(정렬되어 있지 않음)
- 출력 : 
    (움직인 위치 값들의 합)의 최대 값

아이디어
리스트를 차례차례 순회하며 m번만큼 이동했을 때의 합을 구한뒤 최대값을 업데이트 한다.
"""

n,m = map(int, input().split())

data = [0]
data.extend(list(map(int, input().split())))
# [0, 5, 1, 4, 2, 3]


answer = 0

# 탐색을 시작할 원소
for i in range(1, len(data)):
    count = 0

    # 탐색할 인덱스
    chkIndex = i

    # 탐색을 시작할 원소 i 를 바탕으로 m번 탐색
    for k in range(m):
        count += data[i]
        i = data[i]
    answer = max(answer,count)

print(answer)