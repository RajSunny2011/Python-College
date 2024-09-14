# 2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
def sumOfCube(a):
    if a==1:
        return 1
    return (a**3)+sumOfCube(a-1)
a = int(input("Enter a positive integer: "))
print("Sum of Cubes: "+sumOfCube(a))