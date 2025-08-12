n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
wordDict = {}

for word in words:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

counts = wordDict.values()
print(max(counts))