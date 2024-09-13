n = int(input())  # n개의 수
arr = list(map(int, input().split()))  # 주어진 n개의 수 리스트

# 중복 제거 후 정렬
unique_sorted = sorted(set(arr))

# 두 번째로 작은 수가 존재하는지 확인
if len(unique_sorted) <= 2:
    print(-1)
else:
    second_min = unique_sorted[1]  # 두 번째로 작은 수
    # 해당 수의 위치를 출력 (1부터 시작하므로 +1)
    print(arr.index(second_min) + 1)