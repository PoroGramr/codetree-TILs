n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
numDict = {}

for i,word in enumerate(words):
    if i == 0:
        continue
    
    numDict[word] = i

reverseDict = dict(map(reversed, numDict.items()))

for query in queries:
    if query.isdigit():
        num = int(query)
        print(reverseDict[num])
    else:
        print(numDict[query])

