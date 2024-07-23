def chcek(data):
    count = []
    data = list(data)
    for i in range(len(data)):
        if data[i] in count:
            print("Yes")
            return
        else:
            count.append(data[i])

    print("No")
    return 


data  = input()
chcek(data)