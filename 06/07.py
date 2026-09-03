n = int(input("Enter n: "))
sum = 0
for i in range(0,n+1,2):
    sum+=i
print("Sum of Even numbers till ", n, "is:", sum)