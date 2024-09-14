#generators are func which creates a list with any condition attached to it 
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(100)))

def numbers(x):
    i = 0
    while i < x:
        if i % 2 == 0:
            yield i
            i += 1
print(list(numbers(100)))

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
l=list(numbers(11))
print(l)
