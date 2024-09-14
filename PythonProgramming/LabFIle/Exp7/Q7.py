# 7.	Write functions to explain mentioned concepts:
#       a.	Keyword argument
#       b.	Default argument
#       c.	Variable length argument
def name(first,last="Raj"):
    return first+" "+last
print(name(first="Satvik"))
def name2(*args):
    b = ""
    for i in args:
        b+=i+" "
    return b
print(name2("Satvik","Raj","Gupta"))
