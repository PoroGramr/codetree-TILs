def check_num(n):
    if n % 2 != 0:
        return "No"
    
    is_digit = sum(int(i) for i in str(n))

    if is_digit % 5 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())
answer = check_num(n)
print(answer)