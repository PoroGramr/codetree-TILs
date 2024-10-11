n, m = map(int, input().split())

d = dict()

for i in range(n):
    com = str(input())
    d[i + 1] = com

    
for _ in range(m):
    com = input()
    if com.isdigit():
        com = int(com)
        print(d[com])
    else:
        for j in range(1,len(d)):
            if d[j] == com:
                print(j)