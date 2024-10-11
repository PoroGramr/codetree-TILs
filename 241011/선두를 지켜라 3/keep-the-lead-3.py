N, M = map(int, input().split())

dataN = []
for _ in range(N):
    v, t = map(int, input().split())
    dataN.append([v,t])

dataM = []
for _ in range(M):
    v, t = map(int, input().split())
    dataM.append([v,t])

disN = [0] * 1001 # N의 시간별 위치
disM = [0] * 1001 # M의 시간별 위치

nx = 1
for k in range(len(dataN)):
    cur = dataN[k]
    for m in range(cur[1]):
        if nx == 1:
            disN[nx] += cur[0]
            nx += 1
        else:
            disN[nx] += disN[nx - 1] + cur[0]
            nx += 1

mx = 1
for k in range(len(dataM)):
    cur = dataM[k]
    for m in range(cur[1]):
        if mx == 1:
            disM[mx] += cur[0]
            mx += 1
        else:
            disM[mx] += disM[mx - 1] + cur[0]
            mx += 1


time = 0
for i in range(len(dataN)):
    time += dataN[i][1]
ans = 0

curK = []
excurK = []
for t in range(1, time):
    if disN[t] < disM[t]:
        curK = []
        curK.append("M")
    elif disN[t] > disM[t]:
        curK = []
        curK.append("N")
    elif disN[t] == disM[t]:
        curK = []
        curK.append("N")
        curK.append("M")
    if curK != excurK:
        ans += 1
        excurK = curK

print(ans)