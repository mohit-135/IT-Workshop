n = int(input("Enter n: "))
sum = 0
for i in range(1,n,2):
    sum+=i
print("Sum of first", n, "odd numbers is:", sum)