x = int(input("Enter x :"))
n = int(input("Enter n :"))
sum = 0
i = 1
while(i<n+1):
    if(i%2 != 0):
        sum+=x**i
    if(i%2 == 0):
        sum-=x**i
    i+=1
print(sum)