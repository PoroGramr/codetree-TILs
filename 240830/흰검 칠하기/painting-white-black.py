"""
문제 이해
"x L" 의 경우 왼쪽으로 이동하며 x 칸의 타일을 흰색으로 칠함
"x R" 의 경우 오른쪽으로 이동하며 x 칸의 타일을 검은색으로 칠함
덧칠해지면 마지막으로 칠해진 색으로 바뀜 
만약 흰색과 검은색으로 각각 2번이상 칠해지면 회색으로 바뀌고 더이상 바뀌지 않음
모든 명령을 실행한 뒤 흰색, 검은색, 회색의 타일 수를 각각 출력해야 함. 

아이디어

N = 1000 총 타일의 개수는 상수로 

현재 타일의 정보를 담은 리스트 선언
currentTile = [0] * N (0 : 칠해지지 않음, 1 : 흰색, 2: 검정, 3: 회색)

흰색으로 몇번 칠해졌는지 저장하는 리스트 선언
whiteTile = [0] * N

검정으로 몇번 칠해졌는지 저장하는 리스트 선언
blackTile = [0] * N

입력에 따라 반복문을 돌며 3개의 리스트를 업데이트
    - 만약 whiteTile or blackTile 이 >= 2 라면 
        currentTile = 3


"""

TILE = 1000000 # 타일의 개수는 1,000개로 설정

currentTile = [0] * TILE # (0 : 칠해지지 않음, 1 : 흰색, 2: 검정, 3: 회색)

whiteTile = [0] * TILE

blackTile = [0] * TILE

tileX = 499999 # 현재 타일의 좌표

n = int(input())

for i in range(n):
    move, dir = map(str, input().split())
    move = int(move)

    # 방향이 R일때
    if dir == "R":
        for j in range(move):
            # 만약 타일이 회색이라면 스킵
            if currentTile[tileX + j] == 3: 
                continue
            
            # 현재 타일의 색을 검정으로 바꾸고
            # 검정 타일 카운트 +1
            else:
                currentTile[tileX + j] = 2
                blackTile[tileX + j] += 1
        # 현재 타일 정보 반영
        tileX += move - 1

    
    # 방향이 L일때
    else:

        for j in range(move):
            # 만약 타일이 회색이라면 스킵
            if currentTile[tileX - j] == 3:
                continue
            else:
                # 현재 타일의 색을 흰색으로 바꾸고
                # 흰색 타일 카운트 +1
                currentTile[tileX - j] = 1
                whiteTile[tileX - j] += 1

         # 현재 타일 정보 반영
        tileX -= move - 1

    for color in range(TILE):
        if whiteTile[color] >=2 and blackTile[color] >= 2:
            currentTile[color] = 3
    
    # for i in range(495, 515):
    #     print(i - 499 , ":", currentTile[i], ",", end="")
    # print()
"""
-4 : 0 ,-3 : 0 ,-2 : 0 ,-1 : 0 ,0 : 2 ,1 : 2 ,2 : 2 ,3 : 2 ,4 : 0 ,5 : 0 ,6 : 0 ,7 : 0 ,8 : 0 ,9 : 0 ,10 : 0 ,11 : 0 ,12 : 0 ,13 : 0 ,14 : 0 ,15 : 0 ,
-4 : 0 ,-3 : 0 ,-2 : 0 ,-1 : 1 ,0 : 1 ,1 : 1 ,2 : 1 ,3 : 1 ,4 : 0 ,5 : 0 ,6 : 0 ,7 : 0 ,8 : 0 ,9 : 0 ,10 : 0 ,11 : 0 ,12 : 0 ,13 : 0 ,14 : 0 ,15 : 0 ,
-4 : 0 ,-3 : 0 ,-2 : 0 ,-1 : 2 ,0 : 3 ,1 : 3 ,2 : 3 ,3 : 3 ,4 : 2 ,5 : 2 ,6 : 0 ,7 : 0 ,8 : 0 ,9 : 0 ,10 : 0 ,11 : 0 ,12 : 0 ,13 : 0 ,14 : 0 ,15 : 0 ,
-4 : 0 ,-3 : 0 ,-2 : 0 ,-1 : 2 ,0 : 3 ,1 : 3 ,2 : 3 ,3 : 3 ,4 : 1 ,5 : 1 ,6 : 0 ,7 : 0 ,8 : 0 ,9 : 0 ,10 : 0 ,11 : 0 ,12 : 0 ,13 : 0 ,14 : 0 ,15 : 0 ,
"""


gray, white, black = 0 , 0, 0
for countColor in currentTile:
    if countColor == 1:
        white += 1
    elif countColor == 2:
        black += 1
    elif countColor == 3:
        gray += 1

print(white, black, gray)