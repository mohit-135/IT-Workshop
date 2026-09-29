def pow(x , n):
    if(n == 0):
        return 1
    return x*pow(x,n-1)

x = int(input("Enter x :"))
n = int(input("Enter n :"))

print("X to the power N is :",pow(x,n))