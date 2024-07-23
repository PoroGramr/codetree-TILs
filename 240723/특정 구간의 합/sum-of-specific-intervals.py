a,b = map(int, input().split())

global data

data = list(map(int, input().split()))


for i in range(0,b):

    c,d  = map(int, input().split())
    answer = 0
    for i in range(c,d+1):
        answer += data[i - 1]

    print(answer)