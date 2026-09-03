n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        if( i == 0 or i == n - 1 or j == 0 or j == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

i = 0

while i < n:
    j = 0

    while j < n:
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
        
        j += 1

    print()
    i += 1