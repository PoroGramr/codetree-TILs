n = int(input())
curSeat = list(map(int,input()))
answer = 0
for k in range(1,n):
    copySeat = curSeat[::]
    if copySeat[k] == 1:
        continue
    else:
        copySeat[k] = 1
        count = 0
        compare = []
        for j in range(len(copySeat)):
            if copySeat[j] == 0:
                count += 1
            else:
                if count >= 1:
                    compare.append(count)
                count = 0
        compareMin = min(compare)
        answer = max(answer, compareMin)

print(answer)