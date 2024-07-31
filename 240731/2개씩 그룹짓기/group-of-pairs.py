def minimize_max_group_sum(N, numbers):
    # 숫자 정렬
    numbers.sort()

    # 그룹별 합을 저장할 리스트
    group_sums = []

    # 양 끝에서부터 그룹을 짓기
    for i in range(N):
        group_sum = numbers[i] + numbers[2 * N - 1 - i]
        group_sums.append(group_sum)

    # 그룹의 합 중 최댓값을 반환
    return max(group_sums)

# 입력 처리
N = int(input())
numbers = list(map(int, input().strip().split()))

# 결과 출력
result = minimize_max_group_sum(N, numbers)
print(result)