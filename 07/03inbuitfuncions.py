
print("program 1")

mylist = [0, 1, 1]
x = all(mylist)
print(x)


print("program 2")

mylist = [False, True, False]
x = any(mylist)
print(x)


print("program 3")

x = bin(36)
print(x)


print("program 4")

x = bool(1)
print(x)


print("program 5")

x = bytes(4)
print(x)


print("program 6")

x = divmod(5, 2)
print(x)


print("program 7")

x = ("apple", "banana", "cherry")
y = enumerate(x)
print(list(y))


print("program 8")

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)

for x in adults:
    print(x)


print("program 9")

x = float(3)
print(x)


print("program 10")

x = format(0.5, '%')
print(x)


print("program 11")

mylist = ["apple", "banana", "cherry"]
x = frozenset(mylist)
print(x)


print("program 12")

x = hex(255)
print(x)


print("program 13")

x = int(3.5)
print(x)


print("program 14")

mylist = ["apple", "orange", "cherry"]
x = len(mylist)
print(x)


print("program 15")

x = list(("apple", "banana", "cherry"))
print(x)


print("program 16")

x = max(5, 10)
print(x)


print("program 17")

x = min(5, 10)
print(x)


print("program 18")

x = pow(4, 3)
print(x)


print("program 19")

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)

for x in ralph:
    print(x)


print("program 20")

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

x= ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
