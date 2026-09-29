def isPrime(a):
    for i in range(1,a,1):
        if(a%i == 0):
            return 1
    return 0

a = int(input("Enter a Number : "))

result = isPrime(a)
if(result ==1):
        print("Number is NotPrime")
if(result ==0):
        print("Number is Prime")

