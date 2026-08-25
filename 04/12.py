n = int(input("enter a number : "))
sum = 0
i=1
while(i<=2*n-1):
    factorial = 1
    j=1
    while(j<=i):
        factorial = factorial * j
        j+=1
    sum = sum + factorial
    i+=2

print("The sum of the series is :",sum)