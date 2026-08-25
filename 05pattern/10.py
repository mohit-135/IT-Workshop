n = 5

# Roof
for i in range(n):
    print(" " * (n - i), end="")

    if i == 0:
        print("* " * 17)
    else:
        print("*" + " " * (2 * i + 1) + "*")

# Horizontal line
print("* " * 18)

# Walls + door
for i in range(7):
    print("*" + " " * 7, end="")

    if i >= 2:
        print("*" + " " * 9 + "*", end="")

    print(" " * 7 + "*")

# Bottom
print("* " * 18)