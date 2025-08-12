n = int(input())

# Please write your code here.


visited = [False] * (n + 1)
answer = []


def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def choose(curNum):
    if curNum == n + 1:
        print_answer()
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        choose(curNum + 1)
        answer.pop()
        visited[i] = False

choose(1)