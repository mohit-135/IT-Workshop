n = int(input("Enter n: "))

for i in range(1, n + 1):
    term = 5 * i

    if i % 2 == 1:
        term = -term

    print(term, end=" ")