def dfs(y, x):
    # 현재 위치를 방문 처리
    v[y][x] = 1
    count = 1  # 현재 위치 사람 카운트
    
    # 상하좌우 네 방향 탐색
    for py, px in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny, nx = y + py, x + px
        # 영역 안에 있고, 사람이 있으며, 아직 방문하지 않은 경우
        if 0 <= ny < N and 0 <= nx < N and data[ny][nx] == 1 and v[ny][nx] == 0:
            count += dfs(ny, nx)  # 재귀적으로 DFS를 호출하고, 사람 수를 누적
    
    return count

N = int(input())  # 영역 크기 입력
data = [list(map(int, input().split())) for _ in range(N)]  # 지도 데이터 입력
v = [[0 for _ in range(N)] for _ in range(N)]  # 방문 여부 저장 배열
answer = []

# 모든 좌표를 탐색하며 DFS 실행
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and v[i][j] == 0:  # 사람이 있고 아직 방문하지 않은 경우
            answer.append(dfs(i, j))  # 새로운 마을 발견, DFS로 탐색하여 마을 사람 수 추가

# 결과 출력
answer.sort()  # 오름차순 정렬
print(len(answer))  # 총 마을의 수
for cnt in answer:
    print(cnt)  # 각 마을의 사람 수 출력