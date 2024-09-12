# n = int(input())
# curSeat = list(map(int,input()))
# answer = 99999999
# # 모든 자리를 1로 바꿔보는 완전탐색
# for k in range(1,n):

#     # 배열을 복사
#     copySeat = curSeat[::]

#     # 만약 해당 자리가 1이라면(앉아있다면) 스킵
#     if copySeat[k] == 1:
#         continue
    
#     # 해당 자리가 0이라면
#     else:
#         # 해당 자리를 1로 변경 후
#         copySeat[k] = 1

#         # 0이 연속되는 횟수를 체크(빈자리의 길이)
#         count = 0

#         # 0이 연속되는 횟수를 카운트 하고 compare에 삽입
#         compare = []
#         for j in range(len(copySeat)):
#             if copySeat[j] == 0:
#                 count += 1
#             else:
#                 if count >= 1:
#                     compare.append(count + 1)
#                 count = 0

#         # print(copySeat)
#         # print(compare)
#         # 0이 연속되는 횟수중 가장 적은 횟수(가장 가까운 거리)를 추출
#         compareMin = min(compare)
        
#         # 이전 반복문에서의 결과들과 비교
#         answer = min(answer, compareMin)

# print(answer)

import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
seats = list(input())

# Step1. 최적의 위치 찾기
# 인접한 쌍들 중 가장 먼 1간의 쌍을 찾습니다.
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                # 1간의 쌍을 골랐을 때
                # 두 좌석간의 거리가 지금까지의 최적의 답 보다 더 좋다면
                # 값을 갱신해줍니다.
                if j - i > max_dist:
                    max_dist = j - i

                    # 이때, 두 좌석의 위치를 기억합니다.
                    max_i, max_j = i, j
                
                # 인접한 쌍을 찾았으므로 빠져나옵니다.
                break

# Step2. 최적의 위치에 1을 놓습니다.
# 가장 먼 쌍의 위치 가운데에 놓으면 됩니다.
seats[(max_i + max_j) // 2] = '1'

# Step3. 이제 인접한 쌍들 중 가장 가까운 1간의 쌍을 찾습니다.
# 이때의 값이 답이 됩니다.
ans = INT_MAX
for i in range(n):
    if seats[i] == '1':
        for j in range(i + 1, n):
            if seats[j] == '1':
                ans = min(ans, j - i)

                # 인접한 쌍을 찾았으므로 빠져나옵니다.
                break

print(ans)