A = int(input("Enter Side A: "))
B = int(input("Enter Side B: "))
C = int(input("Enter Side C: "))
S = (A+B+C)/2
Area = (S*(S-A)*(S-B)*(S-C))**0.5
print("Area = ",Area)
