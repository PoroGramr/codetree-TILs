days = [31,28,31,30,31,30,31,31,30,31,30,31,0,0,0,0,0,0,0,0,0,0,0]

def checkDay(a,b):
    if days[a-1] >= b:
        return "Yes"
    else:
        return "No"

a,b = map(int,input().split())

answer = checkDay(a,b)
print(answer)