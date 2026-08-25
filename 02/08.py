num = int(input("Enter a three-digit number: "))

a = num % 10
b = (num // 10) % 10
c = num // 100

reverse = a * 100 + b * 10 + c

print("Reversed number:", reverse)