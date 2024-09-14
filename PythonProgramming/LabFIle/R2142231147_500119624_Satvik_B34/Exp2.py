x = 9
y = 7
z = x+y
print("Sum: ",z)
z = x-y
print("Difference: ",z)
z = x*y
print("Multiplication: ",z)
z = x/y
print("Division: ",z)

pi = 3.14159265359
r = int(input("Enter radius of the circle: "))
area = pi*(r**2)
print("Area = ",area)

x = 4
y = 3
z = (x+y)*(x+y)
print(z)

perp = int(input("Enter the perpendicular of the triangle: "))
base = int(input("Enter the base of the triangle: "))
hypo = ((perp)**2+(base)**2)**(1/2)
print(hypo)
Principal_amount = eval(input("Enter principle amount: "))
Rate_of_interest = eval(input("Enter annual rate: "))
Time = eval(input("Enter time (in years): "))
Amount = Principal_amount*(1+(Rate_of_interest/100)*Time)
print("Total ammount =",int(round(Amount,2)))

A = int(input("Enter Side A: "))
B = int(input("Enter Side B: "))
C = int(input("Enter Side C: "))
S = (A+B+C)/2
Area = (S*(S-A)*(S-B)*(S-C))**0.5
print("Area = ",Area)

sec =  int(input("Enter seconds: "))
hour = sec//3600
remsec = sec%3600
minute = remsec//60
remsec = remsec%60
print(f"{hour}h {minute}m {remsec}s")

a = int(input("Enter First Number: "))
v = int(input("Enter Second Number: "))
a = a+v
v = a-v
a = a-v
print("First: ",a,"Second: ",v)

n = int(input("Enter a number: "))
A = (n*(n+1))/2
print(A)
L1 = [0,0,1,1]
L2 = [0,1,0,1]
print("A  B  &  |  ^")
for i in range(0,4):
    print(f"{L1[i]}  {L2[i]}",L1[i]&L2[i],L1[i]|L2[i],L1[i]^L2[i],sep="  ")
a = int(input("Enter a number: "))
l = a<<1
r = a>>1
print(f"Left Shift = {l} Right Shift = {r}")
L = [10,20,56,78,89]
i = int(input("Enter a number: "))
if i in L:
    print("Number is present in the list")
else:
    print("Number is not present in the list")
A = "Satvik Raj"
i = input("Enter a Character: ")
if i in A:
    print("Number is present in string")
else:
    print("Number is not present in string")
