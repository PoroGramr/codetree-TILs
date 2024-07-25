def find_max(arr, n):
    # 기본 사례: 리스트에 하나의 원소만 남은 경우, 그 원소가 최댓값이다.
    if n == 1:
        return arr[0]
    
    # 나머지 배열에서의 최댓값을 찾는다.
    max_of_rest = find_max(arr, n - 1)
    
    # 현재 원소와 나머지 배열의 최댓값을 비교하여 더 큰 값을 반환한다.
    return max(arr[n - 1], max_of_rest)

# 입력 처리
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 최댓값을 찾기 위해 재귀 함수 호출
maximum = find_max(numbers, n)

# 최댓값 출력
print(maximum)