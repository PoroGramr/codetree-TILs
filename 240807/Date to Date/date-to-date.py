numOfDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a,b,c,d = map(int, input().split())
firstDay = 0
for i in range(0,a):
    firstDay += numOfDays[i]
firstDay += b

secondDay = 0
for i in range(0,c):
    secondDay += numOfDays[i]
secondDay += d

print(secondDay-firstDay + 1)