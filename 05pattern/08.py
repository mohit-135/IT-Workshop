n = int(input("Enter n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    if i == 0:
        print("*")
    else:
        print("*", end="")
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*")

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")

    if i == 0:
        print("*")
    else:
        print("*", end="")
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*")

#while loop implementation
i = 0
while i < n:
    j = 0
    while j < n - i - 1:
        print(" ", end="")
        j += 1

    if i == 0:
        print("*")
    else:
        print("*", end="")

        j = 0
        while j < 2 * i - 1:
            print(" ", end="")
            j += 1

        print("*")

    i += 1


i = n - 2
while i >= 0:
    j = 0
    while j < n - i - 1:
        print(" ", end="")
        j += 1

    if i == 0:
        print("*")
    else:
        print("*", end="")

        j = 0
        while j < 2 * i - 1:
            print(" ", end="")
            j += 1

        print("*")

    i -= 1