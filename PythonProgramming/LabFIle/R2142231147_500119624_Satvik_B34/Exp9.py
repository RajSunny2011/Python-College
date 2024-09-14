# 1. Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by taking inputs from the user and display details of all students.
# 2. Add constructor in the above class to initialize student details of n students and implement following methods:
#       a)	Display() student details
#       b)	Find Marks_percentage() of each student
#       c)	Display result() [Note: if marks in each subject >40% than Pass else Fail]
#    Write a Function to find average of the class.

class student:
    count = 0
    def __init__(self,name = "",sap_Id = -1,marks = []):
        self.name = name
        self.sap_Id = sap_Id
        self.marks = marks
        student.count += 1
    def display(self):
        print(f"\nName: {self.name}\nSAP ID: {self.sap_Id}\nMarks-\n  Physics: {marks[0]}\n  Chemistry: {marks[1]}\n  Maths: {marks[2]}")
    def totalPercentage(self):
        return(round(sum(self.marks)/len(self.marks),2))
    def result(self):
        if all(x > 40 for x in self.marks):
            return "PASS"
        return "FAIL"

def average(*students):
    Total = 0
    for i in students:
        Total += i.totalPercentage()
    return round(Total/student.count,2)

s1,s2,s3 = student(),student(),student()

for i in (s1,s2,s3):
    na = input("Enter Name of the student: ")
    sap_Id = int(input("Enter the SAP ID of the student: "))
    marks = []
    phy = float(input("Enter marks in Physics: "))
    marks.append(phy)
    chem = float(input("Enter marks in Chemistry: "))
    marks.append(chem)
    math = float(input("Enter marks in Maths: "))
    marks.append(math)
    i.name,i.sap_Id,i.marks = na, sap_Id, marks

for i in (s1,s2,s3):
    i.display()
    print(f"Total percentage of Student {i.name} = {i.totalPercentage()}%")
    print(f"Result of Student {i.name} is {i.result()}")

print(f"Class Average = {average(s1,s2,s3)}")

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

# Q4. Create a class to implement method Overriding
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

# Q5. Create a class for operator overloading which adds two Point Objects where Point has x & y values
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

P1 = Point(10, 20)
P2 = Point(12, 15)

P3 = P1 + P2

print(P3)
