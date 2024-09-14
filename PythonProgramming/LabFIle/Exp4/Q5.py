# Q5) Check whether given number is palindrome or not.
num = int(input("Enter a number: "))
orig = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if orig == rev:
    print(f"{orig} is a palindrome.")
else:
    print(f"{orig} is not a palindrome.")
