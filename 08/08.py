def sumOfNum(n):
    sum = 0
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        sum+=digit

    return sum


num = int(input("Enter an integer: "))

result = sumOfNum(num)

print("sum of digits of number is:", result)