s = "success"
ch = input("Enter a character: ")

for i in range(len(s)):
    if s[i] == ch:
        print("Character found at index:", i)