# 5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a = int(input("Enter coefficent 'A': "))
b = int(input("Enter coefficent 'B': "))
c = int(input("Enter coefficent 'C': "))
D = (b*b) - (4*a*c)
if D>0:
    r1 = (-b + (D**0.5)) / (2*a)
    r2 = (-b - (D**0.5)) / (2*a)
    print(f"The roots of the equation are = {r1},{r2}")
elif D==0:
    r = -b/(2*a)
    print(f"The root of the equation is = {r}")
else:
    print("There are no real roots of the equation.")
