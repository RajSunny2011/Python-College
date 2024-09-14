# Q1) Find a factorial of given number.
n = int(input("Enter a number: "))
Fact = 1
for i in range(1, n + 1):
    Fact *= i
print(f"The factorial of {n} is {Fact}.")
