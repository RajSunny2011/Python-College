
#A recursive func is a func that can be represented as f(x) = g(x-1)
def factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

print(factorial(0))



def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(3))
print(is_even(2))