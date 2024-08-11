class bomb:
    def __init__(self, code, lineColor, sec):
        self.code = code
        self.lineColor = lineColor
        self.sec = sec

code , lineColor, sec = map(str, input().split())
bomb1 = bomb(code,lineColor,sec)

print("code : ", end = "")
print(code)
print("color : ", end = "")
print(lineColor)
print("second : ", end = "")
print(sec)