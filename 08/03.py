def maxMin(a,b):
    if(a>b):
        return a
    return b

a = int(input("Enter a : "))
b = int(input("Enter b : "))

result = maxMin(a,b)

print(result," is bigger ")
