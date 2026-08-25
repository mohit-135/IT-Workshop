char = (input("Enter a Character :"))

if(char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z'):
    print("Character is an Alphabet")
if(char >= '0' and char <= '9'):
    print("Character is a Digit")
else:
    print("Character is a Special Character")