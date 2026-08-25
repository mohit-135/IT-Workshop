x = int(input("Enter x :"))
n = int(input("Enter n :"))
sum = 0
for i in range(1,2*n+1,2):
    sum+=x**i
print(sum)