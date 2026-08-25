a = int(input("Enter length of side one :"))
b = int(input("Enter length of side two :"))
c = int(input("Enter length of side three :"))



if(a+b > c and b+c > a and a+c > b):
    print("Triangle is valid .")
else:
    print("Triangle is invalid")