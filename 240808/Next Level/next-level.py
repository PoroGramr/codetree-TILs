class user:
    def __init__(self, id = "codetree", level = 10):
        self.id = id
        self.level = level


id, level = map(str, input().split())

user1 = user()

user2 = user(id,level)
print("user", end =" ")
print(user1.id, end =" ")
print("lv", end =" ")
print(user1.level)

print("user", end =" ")
print(user2.id, end =" ")
print("lv", end =" ")
print(user2.level)