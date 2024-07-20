def main():
    n = int(input())
    data = list(map(int,input().split()))
    for i in range(0, n):
        if data[i] % 2 == 0:
            data[i] = data[i] // 2
    
    for i in data:
        print(i, end=" ")

main()