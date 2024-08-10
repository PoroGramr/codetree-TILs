class member:
    def __init__(self, name, score):
        self.name = name
        self.score = score


members = []
for _ in range(5):
    name , score = map(str,input().split())
    members.append(member(name,int(score)))

members.sort(key=lambda x: x.score)

print(members[0].name , end = " ")
print(members[0].score)