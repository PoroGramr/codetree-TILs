def compare(data):
    strData = list(data)
    reverse = []
    for i in range(len(strData)-1,-1,-1):
        reverse.append(strData[i])
    
    if strData == reverse:
        return "Yes"
    else:
        return "No"
        


inputString = input()
print(compare(inputString))