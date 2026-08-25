x = int(input("Enter x :"))
n = int(input("Enter n :"))
sum = 0
for i in range(1,n+1,1):
    sum+=x**i
print(sum)