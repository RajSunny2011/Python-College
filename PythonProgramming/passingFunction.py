def function(func1,func,x):
    return func1(x),func(x)
def square(x):
    return x**2
def cube(x):
    return x**3
c,s = function(cube,square,4)
print(c,s)

