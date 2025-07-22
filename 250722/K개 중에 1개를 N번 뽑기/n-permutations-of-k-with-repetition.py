
K, N = map(int, input().split())

# Please write your code here.
answer = []
def print_answer():
    for e in answer:
        print(e, end=" ")
    print()
def choose(curr_num):
    # 종료 조건
    if curr_num == N + 1:
        print_answer()
        return

    # 반복문을 이용해 0, 1을 선택했을 때 재귀 호출
    for select in range(1,K+1):
        answer.append(select)
        choose(curr_num + 1)
        answer.pop()

    return

choose(1)