class local:
    def __init__(self, name, townNum, city):
        self.name = name
        self.townNum = townNum
        self.city = city


locals = []

n = int(input())
for _ in range(n):
    name, townNum, city = map(str, input().split())
    locals.append(local(name, townNum, city))

locals.sort(key=lambda x: x.name, reverse = True)

print("name " , end = "")
print(locals[0].name)
print("addr " , end = "")
print(locals[0].townNum)
print("city " , end = "")
print(locals[0].city)