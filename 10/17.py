lst = [10, 20, 30]
print("Original list:", lst)

lst.append(40)
print("After append:", lst)

lst.extend([50, 60])
print("After extend:", lst)

lst.insert(1, 15)
print("After insert:", lst)

lst.remove(30)
print("After remove:", lst)

lst.pop()
print("After pop:", lst)