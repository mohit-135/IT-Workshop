n = int(input("enter a number : "))
sum = 0
for i in range(0,2*n+1,1):
    if(i%2 != 0):
        factorial = 1
        for j in range(1,i+1,1):
            factorial = factorial * j
        sum = sum + factorial

print("The sum of the series is :",sum)