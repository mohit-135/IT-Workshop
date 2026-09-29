def first_occurrence(string, character):
    for i in range(len(string)):
        if string[i] == character:
            return i
    return -1


string = input("Enter a string: ")
character = input("Enter a character: ")

result = first_occurrence(string, character)

if result != -1:
    print("First occurrence at index:", result)
else:
    print("Character not found")