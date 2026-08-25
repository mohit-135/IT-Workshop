n = int(input("Enter n: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()