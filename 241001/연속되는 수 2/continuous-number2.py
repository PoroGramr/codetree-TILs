k = int(input())
data = []

# 입력받을 데이터를 리스트에 삽입
for _ in range(k):
    data.append(int(input()))

# 연속된 수 카운트를 위한 변수
count = 0
# 최대로 연속된 값을 계산하기 위한 변수
answer = 0

for i in range(k):
    
    # 첫번째 요소를 검사하거나, 이전 요소와 현재 요소의 값이 연속될 때(같을때)
    if i == 0 or data[i-1] == data[i]:
        count += 1
    
    # 연속되지 않을때
    else:
        count = 1

    # 최대값계산
    answer = max(answer,count)

print(answer)