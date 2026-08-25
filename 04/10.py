n = int(input("enter a number : "))
sum = -1
i=0
while(i<=n):
    factorial = 1
    j=1
    while(j<=i):
        factorial = factorial * j
        j+=1
    sum = sum + factorial
    i+=1

print("The sum of the series is :",sum)