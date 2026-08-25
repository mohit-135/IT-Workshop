a= int(input("enter a :"))
b= int(input("enter b :"))
power = 1
for i in range(1,b+1,1):
    power = power*a

print(a ,"to the power ",b, "is : " , power)