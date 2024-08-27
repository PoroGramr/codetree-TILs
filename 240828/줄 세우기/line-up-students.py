class student:
    def __init__(self, height, kg, num):
        self.height = height
        self.kg = kg
        self.num = num

students = []

n = int(input())


for i in range(n):
    h ,k  = map(int, input().split())
    students.append(student(h, k, i+1))

students.sort(key = lambda x : (-x.height , -x.kg, x.num))

for s in students:
    print(f"{s.height} {s.kg} {s.num} ")