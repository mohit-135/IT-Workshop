n = int(input("Enter n: "))

# Upper half
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()

# Lower half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")

    print()

n = int(input("Enter n: "))

# Upper half
i = 0

while i < n:
    j = 0

    while j < n - i - 1:
        print(" ", end="")
        j += 1

    j = 0

    while j < 2 * i + 1:
        print("*", end="")
        j += 1

    print()
    i += 1


# Lower half
i = n - 2

while i >= 0:
    j = 0

    while j < n - i - 1:
        print(" ", end="")
        j += 1

    j = 0

    while j < 2 * i + 1:
        print("*", end="")
        j += 1

    print()
    i -= 1