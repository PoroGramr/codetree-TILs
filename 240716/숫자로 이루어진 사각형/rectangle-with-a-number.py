n = int(input())
pnum = 1
for _ in range(n):
    for _ in range(n):
        print(pnum , end=" ")
        if pnum == 9:
            pnum =1
        else:
            pnum += 1
        
    print("")