def sumofNaturalNo(n):
    if(n==0):
        return 0
    return n+sumofNaturalNo(n-1)

n = int(input("Enter n :"))

print("The sum of First N natural number is :", sumofNaturalNo(n))
