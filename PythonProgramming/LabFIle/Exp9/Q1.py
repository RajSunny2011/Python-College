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
