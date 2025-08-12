import heapq

N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.

h = []
for command in commands:
    if command[0] == "push":
        heapq.heappush(h,-command[1])
    elif command[0] == "pop":
        print(-heapq.heappop(h))
    elif command[0] == "size":
        print(len(h))
    elif command[0] == "empty":
        if len(h) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        print(-h[0])