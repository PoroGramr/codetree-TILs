"""
문제 이해
- 입력 :
    n,m : 정수,이동횟수
    list : n개의 1~ n 까지의 리스트(정렬되어 있지 않음)
- 출력 : 
    (움직인 위치 값들의 합)의 최대 값

아이디어
- 리스트를 차례차례 순회하며 m번만큼 이동했을 때의 합을 구한뒤 최대값을 업데이트 한다.

중요한 점
- 인덱스 접근이 은근 복잡해 리스트에 첫번째 요소에 None을 추가하니 쉽게 풀렸다.
"""

n,m = map(int, input().split())

# 리스트의 인덱스 접근을 편하게 하기 위해 첫번째 요소에 None 추가
data = [None]
data.extend(list(map(int, input().split())))
# [None, 5, 1, 4, 2, 3]

# 최대값 저장을 위한 변수
answer = 0

# 탐색을 시작할 원소
for i in range(1, len(data)):

    # 원소값들의 합을 저장하기 위한 변수
    count = 0

    # 탐색을 시작할 원소 i 를 바탕으로 m번 탐색
    for k in range(m):
        
        # 움직임 원소값 덧셈
        count += data[i]

        # 다음 탐색할 위치값
        i = data[i]

    # 최대값 업데이트
    answer = max(answer,count)

print(answer)