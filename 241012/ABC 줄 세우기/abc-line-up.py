n = int(input())
data = list(map(str, input().split()))
dataS = sorted(data)

ans = 0
#바꿔줄 인덱스
for k in range(len(data)):
    # 해당 인덱스로 가야할 알파벳 찾기
    for i in range(len(data)):
        # 만약 data[i]와 dataS[k]가 같다
        # -> i를 k의 위치로 옮겨야한다
        if data[i] == dataS[k]:
            # 위치가 같다면 스킵
            if i == k:
                continue
            # 위치가 같지 않다면 1개씩 앞으로 당긴다
            else:
                data[i - 1], data[i] =data[i],data[i - 1]
                ans += 1 
    

print(ans)