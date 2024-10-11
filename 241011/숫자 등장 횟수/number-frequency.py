n, m = map(int, input().split()) # 원소의 개수 n, 질의의 수 m


data= list(map(int, input().split())) # 입력 받은 데이터 리스트

com = list(map(int, input().split())) # 입력 받은 검색해야하는 데이터 리스트

d = dict()  # 딕셔너리 생성

for i in range(n):
    # 만약 딕셔너리에 해당 데이터가 없다면
    if not data[i] in d:
        d[data[i]] = 1
        
    # 있다면 +1
    else:
        d[data[i]] += 1

for j in range(m):
    if com[j] in d:
        print(d[com[j]], end = " ")
    else:
        print(0, end=" ")