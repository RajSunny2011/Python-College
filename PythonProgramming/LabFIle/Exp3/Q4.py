# 4.	Find the greatest among three numbers assuming no two values are same
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1>n2:
    if n1>n3:
        print("First is larger.")
    else:
        print("Third is larger.")
else:
    if n2>n3:
        print("Second is larger.")
    else:
        print("Third is larger.")
