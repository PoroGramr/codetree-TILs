class body:
    def __init__(self, name, height, kg):
        self.name = name
        self.height = height
        self.kg = kg


n = int(input())
bodys = []
for _ in range(n):
    name, height, kg = map(str, input().split())
    bodys.append(body(name,height,kg))

bodys.sort(key=lambda x : x.height)

for a in range(n):
    print(bodys[a].name, bodys[a].height, bodys[a].kg)