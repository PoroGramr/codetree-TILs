"""
문제 이해
기본적으로 모든 칸은 회색임
"x L" 의 경우 왼쪽으로 이동하며 x 칸의 타일을 흰색으로 칠함
"x R" 의 경우 오른쪽으로 이동하며 x 칸의 타일을 검은색으로 칠함
덧칠해지면 마지막으로 칠해진 색으로 바뀜 
모든 명령을 실행한 뒤 흰색, 검은색 타일 수를 각각 출력해야 함. 

아이디어

N = 1000 총 타일의 개수는 상수로 

현재 타일의 정보를 담은 리스트 선언
currentTile = [0] * N (0 : 회색 1 : 흰색, 2: 검정)

for문을 돌며 현재 타일의 색을 바꿔줌

"""

TILE = 10_000 # 타일의 개수는 10,000개로 설정
               

currentTile = [0] * TILE # (0 : 회색, 1 : 흰색, 2: 검정)


tileX = 4_999 # 현재 타일의 좌표

n = int(input())

for i in range(n):
    move, dir = map(str, input().split())
    move = int(move)

    # 방향이 R일때
    if dir == "R":
        for j in range(move):
            # 현재 타일의 색을 검정으로 바꿈
            currentTile[tileX + j] = 2

        # 현재 타일 좌표 정보 반영
        tileX += move - 1

    
    # 방향이 L일때
    else:
        for j in range(move):
            # 현재 타일의 색을 흰색으로 바꿈
            currentTile[tileX - j] = 1

         # 현재 타일 좌표 정보 반영
        tileX -= move - 1

# 각 색별로 카운트
white, black = 0 , 0
for countColor in currentTile:
    if countColor == 1:
        white += 1
    elif countColor == 2:
        black += 1
print(white, black)