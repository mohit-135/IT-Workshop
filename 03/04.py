a = int(input("Enter a num one :"))
b = int(input("Enter a num two :"))
c = int(input("Enter a num three :"))



if(a > b):
    if(a>c):
        print(a," is largest")
    else:
        print(c," is largest")
if(c > a):
    if(c>b):
        print(c," is largest")
    else:
        print(b," is largest")