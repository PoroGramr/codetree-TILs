"""
아이디어
- 크게 가지 케이스가 있음
    - 조합이 변경되는 경우
        - A가 B를 역전
        - B가 A를 역전
        - A가 이기고 있었는데 B가 따라잡음
        - B가 이기고 있었는데 A가 따라잡음

    - 조합이 유지되는 경우

"""

n = int(input())

count = 0
scores = [0, 0] # [A, B] 점수 카운트

exWinner = []
for i in range(n):

    # 첫번쨰 케이스는 따로 지정
    if i == 0:
        stu, score = map(str, input().split())

        if stu == "A":
            scores[0] += int(score)
        elif stu == "B":
            scores[1] += int(score)
        
        # 만약 점수가 0씩 오르는 경우는 스킵
        if int(score) != 0:
            count += 1

        if scores[0] > scores[1]:
            exWinner.append("A")
        else:
            exWinner.append("B")

    

    if i != 0:
        stu, score = map(str, input().split())

        if stu == "A":
            scores[0] += int(score)

        elif stu == "B":
            scores[1] += int(score)

        if int(score) == 0:
            continue
        
        # A가 점수가 더 높은 경우
        if scores[0] > scores[1]:
            # 이전 우슬자가 A라면 스킵
            if len(exWinner) == 1:
                if exWinner[0] == "A":
                    continue

                # 우승자가 달라졌을 경우 카운트 +1 밑 우승자 업데이트
                else:
                    count += 1
                    exWinner.pop()
                    exWinner.append("A")

            # 이전 우승자가 2명이였을 경우
            if len(exWinner) == 2:
                count += 1
                exWinner.pop()
                exWinner.pop()
                exWinner.append("A")
        # B가 점수가 더 높은 경우
        elif scores[0] < scores[1]:
            if len(exWinner) == 1:
                if exWinner[0] == "B":
                    continue
                else:
                    count += 1
                    exWinner.pop()
                    exWinner.append("B")

            if len(exWinner) == 2:
                count += 1
                exWinner.pop()
                exWinner.pop()
                exWinner.append("B")
        
        # 둘의 점수가 같을 경우
        elif scores[0] == scores[1]:
            if len(exWinner) == 1:
                exWinner.pop()
                exWinner.append("A")
                exWinner.append("B")
                count += 1
            elif len(exWinner) == 2:
                continue

print(count)