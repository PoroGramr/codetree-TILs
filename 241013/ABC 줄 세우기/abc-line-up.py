def count_min_swaps(arr):
    swaps = 0
    n = len(arr)

    # 버블 정렬을 활용하여 최소 swap 횟수 구하기
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:  # 두 인접한 사람이 순서가 잘못된 경우
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 위치 교환
                swaps += 1

    return swaps

# 입력 받기
n = int(input())  # 사람 수
arr = input().split()  # 알파벳 순서

# 결과 출력
print(count_min_swaps(arr))