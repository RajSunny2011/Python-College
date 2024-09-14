# Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError
a = input('Enter a Value: ')
b = input('Enter a Value: ')

try:
    a = int(a)
    b = int(b)
    c = a/b
    print(c)
except (ValueError, ZeroDivisionError) as E:
    print("Error:",E)
