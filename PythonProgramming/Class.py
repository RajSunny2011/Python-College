# class MyClass:
#     def __init__(self, arg):
#         print("Hello")
#         self.ar = arg
#         print(self.ar)
# MyClass("5")

class Employee:
    def __init__(self,name,designation,salary):
        self.name = name
        self.designation = designation
        self.salary = salary
    def __str__(self):
        return f"Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}"
employees = []
for i in range(5):
    name = input(f"Enter Employee {i+1}'s Name: ")
    des = input("Enter their Designation: ")
    salary = float(input("Enter their Salary: "))
    employees.append(Employee(name,des,salary))
for i in employees:
    print(i)
