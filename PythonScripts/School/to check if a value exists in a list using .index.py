lst=[1,3,4,5,6]
try:
    lst.index(1)
    print("exist")
except ValueError:
    print("doesn't exist")