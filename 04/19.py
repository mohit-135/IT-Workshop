x = int(input("Enter x :"))
n = int(input("Enter n :"))
sum = 0
for i in range(1,n+1,1):
    if(i%2 != 0):
        sum+=x**i
    if(i%2 == 0):
        sum-=x**i

print(sum)