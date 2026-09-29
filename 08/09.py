def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM =", lcm(num1, num2))