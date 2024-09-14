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
