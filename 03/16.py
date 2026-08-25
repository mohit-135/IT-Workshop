a = int(input("Enter length of side one :"))
b = int(input("Enter length of side two :"))
c = int(input("Enter length of side three :"))

if(a == b and b==c and c==a):
    print("Triangle is Equilateral")
if(a == b or b==c or c==a):
    print("Triangle is Isosceles")
else:
    print("Triangle is scelen")