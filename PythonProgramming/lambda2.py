def myfunction(n):
    return lambda a : a*n
double = myfunction(2)
triple = myfunction(3)
print(double(5))
print(double(6))
print(triple(5))