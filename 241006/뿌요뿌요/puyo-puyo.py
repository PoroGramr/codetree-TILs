import sys
sys.setrecursionlimit(10**5)  # 재귀 깊이 제한을 100,000으로 설정


# 함수 2개 만들 필요 x

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
                
                # dfs를 실행해 블럭의 수를 리턴받음
                tmp = dfsMax(y,x,i)
                
                # 최대값을 big에 저장
                big = max(big,tmp)

bombCount = 0
# 터지게 될 횟수
for i in range(1,100):
    v = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if data[y][x] == i and v[y][x] == 0:
                
                # dfs를 이용해 블럭의 수를 리턴 받음
                # 이때 깨달았다 구지 함수를 2개 만들 필요가 없었단걸
                # 처음엔 dfs함수 리턴값으로 블럭이 4개 이상이라면 블럭의 수를, 4개 미만이라면 0을 리턴하려 했지만 
                # dfs이기에 생각보다 복잡해질거같아 머리를 굴려보니 구지 함수를 2개 만들 필요가 없는걸 깨달았다. 
                bomb = dfsBomb(y,x,i)

                # 만약 블럭의 수가 4이상이라면 -> 터져야하는 경우라면 카운트 +1
                if 4 <= bomb:
                    bombCount += 1

# 결과 출력
print(bombCount, big)