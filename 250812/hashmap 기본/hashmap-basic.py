n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))
calcDict = dict()
# Please write your code here.
for command in commands:
    if command[0] == "add":
        calcDict[command[1]] = command[2]
    elif command[0] == "remove":
        calcDict.pop(command[1])
    elif command[0] == "find":
        if command[1] in calcDict:
            print(calcDict[command[1]])
        else:
            print("None")