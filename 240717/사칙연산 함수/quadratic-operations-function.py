def plus(a,b):
    return a + b

def minus(a,b):
    return a -b

def divide(a,b):
    return a//b

def multi(a,b):
    return a * b

cacu = list(map(str, input().split(" ")))
a = int(cacu[0])
b = int(cacu[2])
answer = cacu[0]
answer += " "
answer += cacu[1]
answer += " "
answer += cacu[2]
answer += " "
answer += "="
answer += " "

if cacu[1] == "+":
    answer += str(plus(a,b))
elif cacu[1] == "-":
    answer += str(minus(a,b))
elif cacu[1] == "/":
    answer += str(divide(a,b))
elif cacu[1] == "*":
    answer += str(multi(a,b))
else: 
    answer = "False"
print(answer)