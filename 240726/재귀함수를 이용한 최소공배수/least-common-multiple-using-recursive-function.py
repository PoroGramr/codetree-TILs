def gcd(a, b):
    """a와 b의 최대공약수를 재귀를 사용하여 반환하는 함수"""
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    """a와 b의 최소공배수를 반환하는 함수"""
    return abs(a * b) // gcd(a, b)

def lcm_of_list(nums, n):
    """숫자 리스트의 LCM을 재귀적으로 계산"""
    # 기본 조건: 리스트에 숫자가 하나만 있는 경우, 그 숫자의 LCM은 자신
    if n == 1:
        return nums[0]
    
    # 재귀 호출: 마지막 숫자와 나머지 숫자들의 LCM을 계산
    return lcm(nums[n-1], lcm_of_list(nums, n-1))

# 입력 처리
n = int(input().strip())  # 첫 번째 줄에서 n을 입력받음
numbers = list(map(int, input().strip().split()))  # 두 번째 줄에서 n개의 수를 입력받아 리스트로 저장

# 결과 출력
result = lcm_of_list(numbers, n)  # n개의 수의 LCM을 계산
print(result)  # 계산된 결과 출력