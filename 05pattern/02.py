n = int(input("Enter n: "))

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

i = 0

while i < n:

    j = 0

    while j < n - i:

        print("*", end="")

        j += 1

    print()

    i += 1