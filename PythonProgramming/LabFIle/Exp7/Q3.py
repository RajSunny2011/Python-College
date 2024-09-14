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