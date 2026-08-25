x = int(input("Enter x :"))
n = int(input("Enter n :"))
sum = 0
i = 1
while(i<=2*n):
    sum+=x**i
    i+=2
print(sum)