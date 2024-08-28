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

# 멘하턴 거리의 맞게 정렬, 거리가 같다면 번호가 작은 점부터 출력
xys.sort(key = lambda x: (abs((0 - x.x)) + abs((0 - x.y)), x.num))

# 요구사항에 맞게 출력
for s in xys:
    print(s.num)