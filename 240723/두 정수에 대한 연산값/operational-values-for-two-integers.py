def check(a,b):
    if a > b:
        print(a + 25, end=" ")
        print(b * 2)
    else:
        print(a * 2, end=" ")
        print(b + 25)
        

        
a,b = map(int,input().split())
check(a,b)