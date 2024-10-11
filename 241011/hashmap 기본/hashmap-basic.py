n = int(input())

d = dict()

for _ in range(n):
    command = list(map(str, input().split()))
    
    if command[0] == "add":
        K, V = int(command[1]), int(command[2])
        d[K] = V
        
    
    elif command[0] == "remove":
        K = int(command[1])
        d.pop(K)

    elif command[0] == "find":
        K = int(command[1])
        if K in d:
            print(d[K])
        else:
            print("None")