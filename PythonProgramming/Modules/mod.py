def gcd(a,b):
    if a==0:
        return b
    return gcd(a%b,a)

def square(num):
    return num*num

def square_root(num):
    return num**0.5

def cube_root(num):
    return num**(1/3)

def cube(num):
    return num*num*num

person = {'name':"john",'age':74,'country':'bangladesh'}