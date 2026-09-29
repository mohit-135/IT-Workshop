def fibonacci(a, b, n):
    if a > n:
        return

    print(a, end=" ")
    fibonacci(b, a + b, n)


n = int(input("Enter the number: "))

fibonacci(0, 1, n)