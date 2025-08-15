n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer = 0
for y in range(0,n-2):
    for x in range(0,n-2):
        
        cnt = 0
        for cy in range(y, y + 3):
            for cx in range(x,x + 3):
                if grid[cy][cx] == 1:
                    cnt += 1

        answer = max(cnt, answer)

print(answer) 