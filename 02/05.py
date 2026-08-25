p = float(input("Enter Principal : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Time : "))

intrest = (p*r*t) / 100
amount = p + intrest

print("Your Intrest is : ",intrest)
print("Total Amount is : ",amount)