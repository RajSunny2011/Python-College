# 3.	Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
if n1>n2:
    print("First number is larger.")
elif n2>n1:
    print("Second number is larger.")
else:
    print("Numbers are equal.")
