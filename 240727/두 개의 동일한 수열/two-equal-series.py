n = int(input())
dataA = list(map(int, input().split()))
dataB = list(map(int, input().split()))
dataA.sort()
dataB.sort()

if dataA == dataB:
    print("Yes")
else:
    print("No")