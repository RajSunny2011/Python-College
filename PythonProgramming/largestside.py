a = int(input("Enter Side A: "))
b = int(input("Enter Side B: "))
c = int(input("Enter Side C: "))
if a>b:
    if a>c:
        print("A is largest side")
    else:
        print("C is largest side")
elif b>c:
    print("B is largest side")
else:
    print("C is largest side")