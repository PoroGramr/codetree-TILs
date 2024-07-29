dataA = input()
dataB = input()
dataA = list(dataA)
dataB = list(dataB)
dataA.sort()
dataB.sort()
dataA = ''.join(dataA)
dataB = ''.join(dataB)
if dataA == dataB:
    print("Yes")
else:
    print("No")