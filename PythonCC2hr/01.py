
# for i in range(1 ,20):
#     if(i%2 !=0):
#         print(i)

# for i in range(1,11,1):
#     print(57 * i)


#list
# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]

# Printing the whole list
print("Complete List:", fruits)

# Accessing elements using index
print("First Fruit:", fruits[0])
print("Third Fruit:", fruits[2])
print("Last Fruit:", fruits[-1])

# List Slicing
print("First 3 Fruits:", fruits[0:3])
print("From Index 2 to End:", fruits[2:])
print("From Start to Index 4:", fruits[:4])
print("Last 2 Fruits:", fruits[-2:])
print("Every 2nd Fruit:", fruits[::2])
print("Reverse List:", fruits[::-1])

# Modifying an element
fruits[1] = "Kiwi"
print("After Modification:", fruits)

# Adding elements
fruits.append("Papaya")
print("After Append:", fruits)

fruits.insert(2, "Cherry")
print("After Insert:", fruits)

# Removing elements
fruits.remove("Orange")
print("After Remove:", fruits)

removed = fruits.pop()
print("Popped Element:", removed)
print("List After Pop:", fruits)

# Length of list
print("Length of List:", len(fruits))

# Loop through list
print("Printing using for loop:")
for item in fruits:
    print(item)

# Check if an item exists
if "Apple" in fruits:
    print("Apple is present.")
else:
    print("Apple is not present.")




#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Tuple^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple")

# Printing the whole tuple
print("Complete Tuple:", fruits)

# Accessing elements using index
print("First Fruit:", fruits[0])
print("Third Fruit:", fruits[2])
print("Last Fruit:", fruits[-1])

# Tuple Slicing
print("First 3 Fruits:", fruits[0:3])
print("From Index 2 to End:", fruits[2:])
print("From Start to Index 4:", fruits[:4])
print("Last 2 Fruits:", fruits[-2:])
print("Every 2nd Fruit:", fruits[::2])
print("Reverse Tuple:", fruits[::-1])

# Length of tuple
print("Length of Tuple:", len(fruits))

# Loop through tuple
print("Printing using for loop:")
for item in fruits:
    print(item)

# Check if an item exists
if "Apple" in fruits:
    print("Apple is present.")
else:
    print("Apple is not present.")

# Count occurrences
numbers = (10, 20, 30, 20, 40, 20)
print("Count of 20:", numbers.count(20))

# Find index of an element
print("Index of 30:", numbers.index(30))