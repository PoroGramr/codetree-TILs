data = list(map(int, input().split()))

if data[0] + 1 == data[1] and data[1] + 1 == data[2]:
    print(0)

elif data[0] + 2 == data[1] or data[1] + 2 == data[2]:
    print(1)
    
else:
    print(2)