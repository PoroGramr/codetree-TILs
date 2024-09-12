n = int(input())
curSeat = list(map(int,input()))
answer = 99999999
# 모든 자리를 1로 바꿔보는 완전탐색
for k in range(1,n):

    # 배열을 복사
    copySeat = curSeat[::]

    # 만약 해당 자리가 1이라면(앉아있다면) 스킵
    if copySeat[k] == 1:
        continue
    
    # 해당 자리가 0이라면
    else:
        # 해당 자리를 1로 변경 후
        copySeat[k] = 1

        # 0이 연속되는 횟수를 체크(빈자리의 길이)
        count = 0

        # 0이 연속되는 횟수를 카운트 하고 compare에 삽입
        compare = []
        for j in range(len(copySeat)):
            if copySeat[j] == 0:
                count += 1
            else:
                if count >= 1:
                    compare.append(count)
                count = 0
                
        # 0이 연속되는 횟수중 가장 적은 횟수(가장 가까운 거리)를 추출
        compareMin = min(compare)
        
        # 이전 반복문에서의 결과들과 비교
        answer = min(answer, compareMin)

print(answer)