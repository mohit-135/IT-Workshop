def isPalindrome(n):
    rev = 0
    original = n
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    if(original==rev):
        return 1
    return 0



num = int(input("Enter an integer: "))

result = isPalindrome(num)

if(result ==1):
        print("Number is Palindrome")
if(result ==0):
        print("Number is NotPalindrome")
