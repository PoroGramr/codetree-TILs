# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

freq = dict()

# 각 숫자가 몇 번씩 나왔는지를
# hashmap에 기록해줍니다.
for elem in arr:
    # 처음 나온 숫자라면 1을 직접 적어줘야 합니다.
    if elem not in freq:
        freq[elem] = 1
    # 이미 나와있던 숫자라면 1을 더해줍니다.
    else:
        freq[elem] += 1

# m개의 질의에 대해
# 몇 번씩 나왔는지를 출력합니다.
queries = list(map(int, input().split()))
for num in queries:
    # 처음 나온 숫자라면 0을 출력합니다.
    if num not in freq:
        print(0, end=" ")
    # 나온 적이 있는 숫자라면, 빈도수를 출력해줍니다.
    else:
        print(freq[num], end=" ")