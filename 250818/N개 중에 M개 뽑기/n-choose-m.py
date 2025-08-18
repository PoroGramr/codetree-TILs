N, M = map(int, input().split())

# Please write your code here.

arr = []

def choose(curNum, cnt):
    if curNum == M + 1:
        if cnt == M :
            tmp = sorted(arr)
            if tmp == arr:
                for a in arr:
                    print(a, end =" ")
                print()
        
        return

    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            choose(curNum + 1, cnt + 1)
        else:
            arr.append(i)
            choose(curNum + 1, cnt)
        arr.pop()


choose(1,0)