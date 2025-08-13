
K, N = map(int, input().split())
answer = []
def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curNum):
    if curNum == N + 1:
        print_answer()
        return
    
    for i in range(1, K + 1):
        answer.append(i)
        choose(curNum + 1)
        answer.pop()

choose(1)