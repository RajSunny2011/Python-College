def function(func1,func,x,y):
    return func1(x,y),func(x,y)
def add(x,y):
    return x+y
def mult(x,y):
    return x*y
s,m = function(add,mult,2,3)
print(s,m)
