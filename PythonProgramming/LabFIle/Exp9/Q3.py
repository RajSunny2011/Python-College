# Q3. Create programs to implement different types of inheritances.

#Single Inheritance-
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
        return f"{super().__str__()} {self.age}"

y = person("Satvik","Raj")
print(y)
x = child("Aman","Singh",12)
print(x)

# MultiLevel inheritance
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
        return f"{super().__str__()} {self.age}"

class student(child):
    def __init__(self, fname, lname, age, school):
        super().__init__(fname, lname, age)
        self.school = school
    def __str__(self):
        return f"{super().__str__()} {self.school}"

y = person("Satvik", "Raj")
print(y)
x = child("Aman", "Singh",12)
print(x)
z = student("Anshuman", "Rangarh", 19, "SOCS")
print(z)

#Multiple Inheritance
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Child(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def __str__(self):
        return f"{super().__str__()} {self.age}"

class School:
    def __init__(self, school_name):
        self.school_name = school_name
    def __str__(self):
        return f"{self.school_name}"

class Student(Child, School):
    def __init__(self, fname, lname, age, school_name):
        Child.__init__(self, fname, lname, age)
        School.__init__(self, school_name)
    def __str__(self):
        return f"{Child.__str__(self)} attends {School.__str__(self)}"

y = Person("Satvik", "Raj")
print(y)
x = Child("Aman", "Singh", 12)
print(x)
z = Student("Anshuman", "Rangarh", 19, "Harvard University")
print(z)
