"""
아이디어
- 수열을 입력받음
- 입력받은 수열을 바탕으로 수열과 수열의 현재위치를 저장하는 클래스를 하나 만든 후 수열의 현재 위치를 저장
- 처음 수열을 정렬
- 정렬된 위치를 저장하는 인스턴스를 생성
- 정렬된 후 처음 위치와 이동된 위치를 비교
"""
n = int(input())

# 입력받은 원소 리스트
oriData = list(map(int, input().split()))

# 입력받은 리스트를 정렬한 후 각 값에 대한 정렬 후의 인덱스를 기록
sortData = sorted((val, idx) for idx, val in enumerate(oriData))

# 정렬된 리스트에서 각 원소의 새로운 위치를 저장할 리스트
answer = [0] * n

# 새로운 위치를 기록
for new_idx, (val, old_idx) in enumerate(sortData):
    answer[old_idx] = new_idx + 1

# 결과 출력
print(" ".join(map(str, answer)))