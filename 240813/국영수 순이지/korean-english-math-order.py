class score:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


n = int(input())
scores = []

for _ in range(n):
    name, korean, english, math = map(str,input().split())
    scores.append(score(name,int(korean), int(english), int(math)))

scores.sort(lambda x: (-x.korean, -x.english, -x.math))

for a in range(n):
    print(scores[a].name, scores[a].korean, scores[a].english, scores[a].math )