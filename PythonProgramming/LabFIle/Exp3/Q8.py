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
