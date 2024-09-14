a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a>b:
    pass
    print("'a' is greater than 'b'",end=" ")
    if a>c:
        print("and 'a' is greater than 'c'")
    else:
        print("and 'a' is smaller than 'c'")
