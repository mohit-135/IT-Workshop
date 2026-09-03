a = int(input("Enter a marks of student1: "))
b = int(input("Enter b marks of student2: "))
c = int(input("Enter c marks of student3: "))
d = int(input("Enter d marks of student4: "))
e = int(input("Enter e marks of student5: "))

if a > b and a > c and a > d and a > e:
    print("Student1 has highest marks")
elif b > a and b > c and b > d and b > e:
    print("Student2 has highest marks")
elif c > a and c > b and c > d and c > e:
    print("Student3 has highest marks")
elif d > a and d > b and d > c and d > e:
    print("Student4 has highest marks")
else:
    print("Student5 has highest marks")


