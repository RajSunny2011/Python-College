# 1.	Check whether given number is divisible by 3 and 5 both
n = int(input("Enter a Number: "))
if n%3==0 and n%5==0:
    print("Entered number is divisible by 3 and 5.")

# 2.	Check whether a given number is multiple of five or not.
n = int(input("Enter a Number: "))
if n%5==0:
    print("Entered number is a multiple of 5.")
else:
    print("Entered number is not a multiple of 5.")

# 3.	Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.
n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
if n1>n2:
    print("First number is larger.")
elif n2>n1:
    print("Second number is larger.")
else:
    print("Numbers are equal.")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1>n2:
    if n1>n3:
        print("First is larger.")
    else:
        print("Third is larger.")
else:
    if n2>n3:
        print("Second is larger.")
    else:
        print("Third is larger.")

# 5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a = int(input("Enter coefficent 'A': "))
b = int(input("Enter coefficent 'B': "))
c = int(input("Enter coefficent 'C': "))
D = (b*b) - (4*a*c)
if D>0:
    r1 = (-b + (D**0.5)) / (2*a)
    r2 = (-b - (D**0.5)) / (2*a)
    print(f"The roots of the equation are = {r1},{r2}")
elif D==0:
    r = -b/(2*a)
    print(f"The root of the equation is = {r}")
else:
    print("There are no real roots of the equation.")

# 6.	Find whether a given year is a leap year or not.
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is leap year.")
else:
    print("Year is not leap year.")

# 7.	Write a program which takes any date as input and display next date of the calendar
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29
day += 1
if day > days_in_month[month-1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(f"The next date is: {day}/{month}/{year}")

# 8.	Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
sapid = input("Enter SAPID: ")
semester = input("Enter semester: ")
course = input("Enter course: ")
subjects = ["PDS", "Python", "Chemistry", "English", "Physics"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)
percentage = sum(marks) / len(marks)
cgpa = percentage / 10
print("\nGradesheet")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}\tSAPID: {sapid}")
print(f"Sem: {semester}\tCourse: {course}\n")
print("Subject name:\tMarks")
for i in range(len(subjects)):
    print(f"{subjects[i]}:\t\t{marks[i]}")
print(f"Percentage: {percentage}%")
print(f"CGPA: {cgpa:.1f}")
if 0 <= cgpa <= 3.4:
    print("Grade: F")
elif 3.5 <= cgpa <= 5.0:
    print("Grade: C+")
elif 5.1 <= cgpa <= 6.0:
    print("Grade: B")
elif 6.1 <= cgpa <= 7.0:
    print("Grade: B+")
elif 7.1 <= cgpa <= 8.0:
    print("Grade: A")
elif 8.1 <= cgpa <= 9.0:
    print("Grade: A+")
elif 9.1 <= cgpa <= 10.0:
    print("Grade: O")
