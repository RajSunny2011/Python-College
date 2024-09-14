def equalCheck(x,y):
    if x == y:
        return "equal"
    elif x > y:
        return "x is greater"
    return "y is greater"
x = int(input("Enter a Number (x): "))
y = int(input("Enter a Number (y): "))
print(equalCheck(x,y))

def swap(x,y):
    return y,x
x = int(input("Enter a Number (x): "))
y = int(input("Enter a Number (y): "))
x,y = swap(x,y)
print("x =",x,"\ny =",y)

def fullName(firstName, lastName):
    return firstName+lastName
f = input("Enter first name: ")
l = input("Enter last name: ")
print(fullName(f,l))

def average(x):
    return sum(x)/len(x)
x = tuple(input("Enter numbers seprated by comma: "))
print(average(x))

def oddOrEven(x):
    if x//2==0:
        return "Even"
    return "Odd"
x = int(input("Enter a number: "))
print(oddOrEven(x))

def secToMin(time):
    return int(time[0])*60+int(time[1])+int(time[2])/60
s = eval(input("Enter time in (hr,min,sec): "))
print(round(secToMin(s),5))

def simpleInterest(principal,time,senior):
    if senior:
        return principal*(1+time*0.12)
    return principal*(1+time*0.1)
def compoundInterest(principal,time,senior):
    if senior:
        return principal*((1+0.12)**time)
    return principal*((1+0.1)**time)
p = int(input("Enter the principal amount: "))
t = int(input("Enter duration of deposit in years: "))
s = int(input("Enter age of customer: "))>59
print("Total amount: ",round(simpleInterest(p,t,s),2))
print("Total amount(compunded): ",round(compoundInterest(p,t,s),2))

def volumeOfCuboid(length = 1,breadth = 1,height = 1):
    return length*breadth*height
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
h = int(input("Enter height: "))
print(volumeOfCuboid(l,b,h))

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
def permutations(n,r):
    if n<r:
        return "Not Valid"
    return fact(n)/fact(n-r)
def combinations(n,r):
    if n<r:
        return "Not Valid"
    return fact(n)/fact(n)*fact(n-r)
n = int(input("Enter number of objects(n): "))
r = int(input("Enter number of places(r): "))
print("Permutaions: ",permutations(n,r))
print("Combinations: ",combinations(n,r))

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
def series(n):
    if n == 1:
        return 1
    return n**n/fact(n)+series(n-1)
n = int(input("Enter a Number: "))
print(series(n))

num = int(input())+1
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
for i in range(num):
    print(fibonacci(i))

def gcd(a,b):
    if a==0:
        return b
    return gcd(a%b,a)
def lcm(a,b):
    return a*b//gcd(a,b)
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(f"LCM of {a},{b} =",lcm(a,b),f"GCD of {a},{b} =", gcd(a,b))
