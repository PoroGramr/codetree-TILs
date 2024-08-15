class score:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3


n = int(input())

datas = []

for _ in range(n):
    name, sub1, sub2, sub3 = map(str, input().split())
    datas.append(score(name, int(sub1), int(sub2), int(sub3)))

datas.sort(key = lambda x: x.sub1+x.sub2+x.sub3)

for i in range(n):
    print(datas[i].name, datas[i].sub1, datas[i].sub2, datas[i].sub3)