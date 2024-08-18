class student:
    def __init__(self, name, height, kg):
        self.name = name
        self.height = height
        self.kg = kg


n = int(input())

school = []

for _ in range(n):
    name, height, kg = map(str, input().split())
    school.append(student(name, int(height), int(kg)))

school.sort(key=lambda x: (x.height, -x.kg))

for i in range(n):
    print(school[i].name, school[i].height, school[i].kg)