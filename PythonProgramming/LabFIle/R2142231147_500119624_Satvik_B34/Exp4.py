# Q1) Find a factorial of given number.
n = int(input("Enter a number: "))
Fact = 1
for i in range(1, n + 1):
    Fact *= i
print(f"The factorial of {n} is {Fact}.")

# Q2) Find whether the given number is Armstrong number.
import math
num = int(input("Enter a number: "))
pow = math.log10(num)+1
a = num
sum = 0
while a > 0:
    digit = a% 10
    sum += digit ** pow
    a //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Q3) Print Fibonacci series up to given term.
term = int(input("Enter the number of terms for Fibonacci series: "))
series = [0, 1]
while len(series) < term:
    series.append(series[-1] + series[-2])
print(f"Fibonacci series up to {term} terms: {series[:term]}")

# Q4) Write a program to find if given number is prime number or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

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

# Q6) Write a program to print sum of digits.
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f"The sum of digits is {sum}")

# Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100.
divby5or7 = [num for num in range(1, 101) if num % 5 == 0 or num % 7 == 0]
print(f"Numbers divisible by 5 or 7 between 1 to 100: {divby5or7}")
print(f"Count: {len(divby5or7)}")

# Q8) Convert all lower cases to upper case in a string.
orig = input("Enter a string: ")
new = orig.upper()
print(f"Original string: {orig}")
print(f"String in upper case: {new}")

# Q9) Print all prime numbers between 1 and 100.
a = 2
while a < 100:
    x = 2
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            break
    else:
        print(a)
    a += 1

# Q10) Print the table for a given number: 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
