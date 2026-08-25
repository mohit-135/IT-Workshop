n = int(input("Enter day of Month : "))

if(n == 1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("The Month has 31 days")
if(n == 4 or n==6 or n==9 or n==11):
    print("The Month has 30 days")
if(n == 2):
    print("The Month has 28 or 29 days")