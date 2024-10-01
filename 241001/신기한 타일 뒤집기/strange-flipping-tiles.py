data = [ 0 for _ in range(1000)]
n = int(input())
cx = 500
for i in range(n):
    x, g = map(str,input().split())
    if g == "R": # 검은색
        x = int(x)
        for k in range(cx, cx + x):
            data[k] = 1
        cx = cx + x - 1
    elif g == "L":
        x = int(x)
        for k in range(cx, cx - x, -1):
            data[k] = 2
        cx = cx - x + 1
cb = 0
cw = 0
for c in data:
    if c == 1:
        cb += 1
    elif c == 2:
        cw += 1

print(cw , cb)