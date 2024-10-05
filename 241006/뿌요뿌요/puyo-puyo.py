import sys
sys.setrecursionlimit(10**5)  # 재귀 깊이 제한을 100,000으로 설정

def dfsMax(y,x,i):
    v[y][x] = 1
    count = 1

    for py, px in ((0,1),(0,-1),(1,0),(-1,0)):
        ny, nx = y + py, x + px
        if 0 <= ny < N and 0 <= nx < N and data[ny][nx] == i and v[ny][nx] == 0:
            count += dfsMax(ny,nx,i)

    return count

def dfsBomb(y,x,i):
    v[y][x] = 1
    count = 1
    for py, px in ((0,1),(0,-1),(1,0),(-1,0)):
        ny, nx = y + py, x + px
        if 0 <= ny < N and 0 <= nx < N and data[ny][nx] == i and v[ny][nx] == 0:
            count += dfsBomb(ny,nx,i)
    return count
    

N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

big = 0
# 최대 블럭의 크기
for i in range(1,100):
    v = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if data[y][x] == i and v[y][x] == 0:
                tmp = dfsMax(y,x,i)
                big = max(big,tmp)

bombCount = 0
# 터지게 될 블럭의 숫자
for i in range(1,100):
    v = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            bomb = dfsBomb(y,x,i)
            if 4 <= bomb:
                bombCount += 1
print(bombCount, big)