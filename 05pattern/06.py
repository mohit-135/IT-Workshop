n = int(input("Enter n: "))

for i in range(1,n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    for j in range(2, i + 1):
        print(j, end=" ")

    print()

n = int(input("Enter n: "))

i = 1

while i <= n:

    # Print spaces
    j = 0
    while j < n - i:
        print(" ", end=" ")
        j += 1

    # Print decreasing numbers
    j = i
    while j >= 1:
        print(j, end=" ")
        j -= 1

    # Print increasing numbers
    j = 2
    while j <= i:
        print(j, end=" ")
        j += 1

    print()
    i += 1