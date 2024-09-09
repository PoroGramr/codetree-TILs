R, C = map(int, input().split()) # 가로 세로 길이

data = []

for _ in range(R):
    data.append(list(map(str, input().split())))

answer = 0

for i in range(1,R): # 0,0은 이미 밟고 시작하기에 1부터 시작
    for k in range(1, C):
        for j in range(i + 1, R - 1): # R,C는 도착 지점이기에 제외
            for a in range(k + 1, C - 1):
                 if data[0][0] != data[i][k] and \
                   data[i][k] != data[j][a] and \
                   data[j][a] != data[R - 1][C - 1]:
                   answer += 1


print(answer)