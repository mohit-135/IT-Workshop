n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(" ", end=" ")

    for j in range(1, n-i , 1):
        print(j, end=" ")

    print()

n = int(input("Enter n: "))

i = 1
while i <= n:
    j = 0
    while j < i:
        print(" ", end=" ")
        j += 1

    j = 1
    while j < n - i:
        print(j, end=" ")
        j += 1

    print()
    i += 1