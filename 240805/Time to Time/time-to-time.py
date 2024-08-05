firstHour , firstMinute, secondHour , secondMinute  = map(int, input().split())


totalFirstMinute = firstHour * 60 + firstMinute
totalSecondMinute = secondHour * 60 + secondMinute

print(totalSecondMinute - totalFirstMinute)