class xy:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num


n = int(input())

xys = []

for i in range(n):
    x, y = map(int, input().split())
    xys.append(xy(x,y, i+1))

xys.sort(key = lambda x: (abs((0 - x.x) + (0 - x.y)), x.num))

for s in xys:
    print(s.num)