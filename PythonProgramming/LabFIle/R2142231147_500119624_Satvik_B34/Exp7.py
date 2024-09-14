# 1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  
def MinMax(ls):
    s = ls[0]
    l = ls[0]
    for i in ls:
        if i>l:
            l=i
        if i<s:
            s=i
    return s,l
ls = [1,2,3]
print(MinMax(ls))
# 2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
def sumOfCube(a):
    if a==1:
        return 1
    return (a**3)+sumOfCube(a-1)
a = int(input("Enter a positive integer: "))
print("Sum of Cubes: "+sumOfCube(a))
# 3.	Write a Python function to print 1 to n using recursion
def print1ToN(a):
    if a==1:
        print(1)
        return 0
    print1ToN(a-1)
    print(a)
    return 0
a = int(input("Enter a positive integer: "))
print1ToN(a)
# 4.	Write a recursive function to print Fibonacci series upto n terms
num = int(input("Enter number of terms: "))
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
for i in range(num):
    print(fibonacci(i),end=" ")
# 5.	Write a lambda function to find volume of cone
pi = 3.14159624
coneVolume = lambda r,h : 0.33333*r*r*h*pi
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
print("Volume of cone = ",coneVolume(r,h))
# 6.	Write a lambda function which gives tuple of max and min from a list.
ls = [1,2,4,1,7]
MinMax = lambda Nums: (max(Nums), min(Nums))
print(MinMax(ls))
# 7.	Write functions to explain mentioned concepts:
#       a.	Keyword argument
#       b.	Default argument
#       c.	Variable length argument
def name(first,last="Raj"):
    return first+" "+last
print(name(first="Satvik"))
def name2(*args):
    b = ""
    for i in args:
        b+=i+" "
    return b
print(name2("Satvik","Raj","Gupta"))
