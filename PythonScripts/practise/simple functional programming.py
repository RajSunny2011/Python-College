def apply_twice(func, arg): #func to apply the a function twice
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

print((lambda x: x**2 + 5*x + 4) (-4))
