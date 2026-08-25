n = int(input("enter a number : "))
sum = 0
i=1
while(i<n+1):
    if(i%2 != 0):
        factorial = 1
        for j in range(1,i+1,1):
            factorial = factorial * j
        sum = sum + factorial
    if(i%2 == 0):
            factorial = 1
            for j in range(1,i+1,1):
                factorial = factorial * j
            sum = sum - factorial
    i+=1

print("The sum of the series is :",sum)