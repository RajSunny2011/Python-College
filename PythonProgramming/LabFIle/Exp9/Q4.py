# Create a class to implement method Overriding
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"

class child(person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def __str__(self):
        return f"{super().__str__()} {self.age}" # this overrides person __str__ method

y = person("Satvik","Raj")
print(y)
x = child("Aman","Singh",12)
print(x)
