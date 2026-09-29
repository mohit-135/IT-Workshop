def area(r):
    return r*r*3.14
def circ(r):
    return 2*3.14*r

r = float(input("Enter Radius of Circle: "))

area = area(r)
circ = circ(r)

print("area of circle is ", area)
print("Circumfarence of circle is ", circ)