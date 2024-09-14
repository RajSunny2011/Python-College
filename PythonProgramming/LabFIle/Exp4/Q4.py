# Q4) Write a program to find if given number is prime number or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
