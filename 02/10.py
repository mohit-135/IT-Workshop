num = int(input("Enter a four-digit number: "))

a = num % 10
b = (num // 10) % 10
c = (num // 100) %10
d = (num // 1000)

a = a+1
b = b+1
c = c+1
d = d+1

num2 = a + b*10 + c*100 + d*1000



print("The new number is :", num2)