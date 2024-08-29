data = [0] * 100

n = int(input())
currentX = 49
for _ in range(n):
    x, direction = map(str, input().split())
    x = int(x)
    storeX = currentX
    cac = 0
    if direction == "R":
        # 오른쪽으로 이동하는 경우
        for i in range(currentX, currentX + x):
            data[i] += 1
        currentX += x  # 현재 위치 업데이트
        
    elif direction == "L":
        # 왼쪽으로 이동하는 경우
        for i in range(currentX, currentX - x, -1):
            data[i] += 1
        currentX -= x  # 현재 위치 업데이트

    
    storeX += cac
    currentX += cac
    # for i in range(38, 55):
    #     print(i - 49 ,":", data[i], ",", end=" ")
    # print("loop")

answer = 0
for i in data:
    if i >= 2:
        answer += 1

print(answer)


"""
-11 : 0 , -10 : 0 , -9 : 0 , -8 : 0 , -7 : 0 , -6 : 0 , -5 : 0 , -4 : 0 , -3 : 0 , -2 : 0 , -1 : 0 , 0 : 1 , 1 : 1 , 2 : 1 , 3 : 0 , 4 : 0 , 5 : 0 , loop
-11 : 0 , -10 : 0 , -9 : 0 , -8 : 0 , -7 : 0 , -6 : 0 , -5 : 0 , -4 : 1 , -3 : 1 , -2 : 1 , -1 : 1 , 0 : 2 , 1 : 2 , 2 : 2 , 3 : 0 , 4 : 0 , 5 : 0 , loop
-11 : 0 , -10 : 0 , -9 : 0 , -8 : 0 , -7 : 0 , -6 : 0 , -5 : 0 , -4 : 2 , -3 : 2 , -2 : 1 , -1 : 1 , 0 : 2 , 1 : 2 , 2 : 2 , 3 : 0 , 4 : 0 , 5 : 0 , loop
-11 : 1 , -10 : 1 , -9 : 1 , -8 : 1 , -7 : 1 , -6 : 1 , -5 : 1 , -4 : 3 , -3 : 3 , -2 : 1 , -1 : 1 , 0 : 2 , 1 : 2 , 2 : 2 , 3 : 0 , 4 : 0 , 5 : 0 , loop
-11 : 2 , -10 : 2 , -9 : 1 , -8 : 1 , -7 : 1 , -6 : 1 , -5 : 1 , -4 : 3 , -3 : 3 , -2 : 1 , -1 : 1 , 0 : 2 , 1 : 2 , 2 : 2 , 3 : 0 , 4 : 0 , 5 : 0 , loop
-11 : 2 , -10 : 3 , -9 : 2 , -8 : 2 , -7 : 1 , -6 : 1 , -5 : 1 , -4 : 3 , -3 : 3 , -2 : 1 , -1 : 1 , 0 : 2 , 1 : 2 , 2 : 2 , 3 : 0 , 4 : 0 , 5 : 0 , loop
9

"""