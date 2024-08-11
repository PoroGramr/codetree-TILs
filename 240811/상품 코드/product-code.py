class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

product1 = product("codetree", "50")

name1, code1 = map(str, input().split())

product2 = product(name1,code1)

print("product ", end="")
print(product1.code, end ="")
print(" is ", end="")
print(product1.name)

print("product ", end="")
print(product2.code, end ="")
print(" is ", end="")
print(product2.name)