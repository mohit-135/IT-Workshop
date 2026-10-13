s = "success"
ch = input("Enter a character to remove: ")

if ch in s:
    i = s.find(ch)
    s = s[:i] + s[i + 1:]

print("String after removal:", s)