n , m = map(int, input().split()) # 원소의 개수 n, 질의의 수 m

data = list(map(int, input().split()))

com = list(map(int, input().split()))

numIn = {}

for i, elem in enumerate(data):
    numIn[i] = elem

for co in com:
    ans = 0
    for k in range(len(numIn)):
        if numIn[k] == co:
            ans += 1
    
    print(ans, end=" ")