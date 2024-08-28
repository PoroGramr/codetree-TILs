class student:
    def __init__(self, cm, kg ,num):
        self.cm = cm
        self.kg = kg
        self.num = num

n = int(input())

data = []

for i in range(n):
    cm , kg = map(int, input().split())
    data.append(student(cm, kg, i+1))

data.sort(key =lambda x : (x.cm , -x.kg))

for s in data:
    print(f"{s.cm} {s.kg} {s.num}")