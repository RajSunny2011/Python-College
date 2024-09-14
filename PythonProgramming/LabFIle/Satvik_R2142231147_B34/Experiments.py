# EXP 1
# Q2. Write Python programs to print strings in the given manner:
# a)   Hello Everyone !!!
# b)   Hello
#       World
# c)   Hello
#               World
# d) ‘ Rohit’ s date of birth is 12\05\1999’

print("Hello Everyone !!!")
print('''Hello
World''')
print('''Hello
    World''')
print("Rohit's date of borth is 12\\05\\1999")

# Q3) Declare a string variable called x and assign it the value “Hello”. Print out the value of x
x="Hello"
print(x)

# Q4) Take different data types and print values using print function.
a,b,c,d = "Hello",14,1.0,[1,2,3]
print(a,b,c,d)

# Q5) Take two variable a and b. Assign your first name and last name. Print your Name after adding your First name and Last name together.
a = "Satvik"
b = "Raj"
print(a,b)

# Q6)   Declare three variables, consisting of your first name, your last name and Nickname. Write a  program that prints out your first name, then your nickname in parenthesis and then your last name.  
First_name = "Satvik"
Last_name = "Raj"
Nick_name = "Sunny"
print("{} ({}) {}".format(First_name, Nick_name, Last_name))

# Q7) Declare and assign values to suitable variables and print in the following way :
# NAME : NIKUNJ BANSAL  
# SAP ID : 500069944
# DATE OF BIRTH : 13 Oct 1999
# ADDRESS : UPES
                    # Bidholi Campus
                    # Pincode : 248007
# Programme : AI & ML                                                                                      
# Semester : 2
Name = "Satvik Raj"
SAP_Id = 500119624
Date_of_birth = "13 oct 1999"
Address = '''UPES
         Bidholi Campus
         Pincode: 248007'''
Batch = 34
Semester = 2
print(f'''Name: {Name}
SAP ID: {SAP_Id}
Date of Birth: {Date_of_birth}
Address: {Address}
Batch: {Batch}
Semester: {Semester}''')


x = 9
y = 7
z = x+y
print("Sum: ",z)
z = x-y
print("Difference: ",z)
z = x*y
print("Multiplication: ",z)
z = x/y
print("Division: ",z)

pi = 3.14159265359
r = int(input("Enter radius of the circle: "))
area = pi*(r**2)
print("Area = ",area)

x = 4
y = 3
z = (x+y)*(x+y)
print(z)

perp = int(input("Enter the perpendicular of the triangle: "))
base = int(input("Enter the base of the triangle: "))
hypo = ((perp)**2+(base)**2)**(1/2)
print(hypo)
Principal_amount = eval(input("Enter principle amount: "))
Rate_of_interest = eval(input("Enter annual rate: "))
Time = eval(input("Enter time (in years): "))
Amount = Principal_amount*(1+(Rate_of_interest/100)*Time)
print("Total ammount =",int(round(Amount,2)))

A = int(input("Enter Side A: "))
B = int(input("Enter Side B: "))
C = int(input("Enter Side C: "))
S = (A+B+C)/2
Area = (S*(S-A)*(S-B)*(S-C))**0.5
print("Area = ",Area)

sec =  int(input("Enter seconds: "))
hour = sec//3600
remsec = sec%3600
minute = remsec//60
remsec = remsec%60
print(f"{hour}h {minute}m {remsec}s")

a = int(input("Enter First Number: "))
v = int(input("Enter Second Number: "))
a = a+v
v = a-v
a = a-v
print("First: ",a,"Second: ",v)

n = int(input("Enter a number: "))
A = (n*(n+1))/2
print(A)
L1 = [0,0,1,1]
L2 = [0,1,0,1]
print("A  B  &  |  ^")
for i in range(0,4):
    print(f"{L1[i]}  {L2[i]}",L1[i]&L2[i],L1[i]|L2[i],L1[i]^L2[i],sep="  ")
a = int(input("Enter a number: "))
l = a<<1
r = a>>1
print(f"Left Shift = {l} Right Shift = {r}")
L = [10,20,56,78,89]
i = int(input("Enter a number: "))
if i in L:
    print("Number is present in the list")
else:
    print("Number is not present in the list")
A = "Satvik Raj"
i = input("Enter a Character: ")
if i in A:
    print("Number is present in string")
else:
    print("Number is not present in string")

# EXP 2
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
# Q1) Find a factorial of given number.
n = int(input("Enter a number: "))
Fact = 1
for i in range(1, n + 1):
    Fact *= i
print(f"The factorial of {n} is {Fact}.")

# Q2) Find whether the given number is Armstrong number.
import math
num = int(input("Enter a number: "))
pow = math.log10(num)+1
a = num
sum = 0
while a > 0:
    digit = a% 10
    sum += digit ** pow
    a //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Q3) Print Fibonacci series up to given term.
term = int(input("Enter the number of terms for Fibonacci series: "))
series = [0, 1]
while len(series) < term:
    series.append(series[-1] + series[-2])
print(f"Fibonacci series up to {term} terms: {series[:term]}")

# Q4) Write a program to find if given number is prime number or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Q5) Check whether given number is palindrome or not.
num = int(input("Enter a number: "))
orig = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if orig == rev:
    print(f"{orig} is a palindrome.")
else:
    print(f"{orig} is not a palindrome.")

# Q6) Write a program to print sum of digits.
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f"The sum of digits is {sum}")

# Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100.
divby5or7 = [num for num in range(1, 101) if num % 5 == 0 or num % 7 == 0]
print(f"Numbers divisible by 5 or 7 between 1 to 100: {divby5or7}")
print(f"Count: {len(divby5or7)}")

# Q8) Convert all lower cases to upper case in a string.
orig = input("Enter a string: ")
new = orig.upper()
print(f"Original string: {orig}")
print(f"String in upper case: {new}")

# Q9) Print all prime numbers between 1 and 100.
a = 2
while a < 100:
    x = 2
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            break
    else:
        print(a)
    a += 1

# Q10) Print the table for a given number: 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#1.	 Write a program to count and display the number of capital letters in a given string.
str=input("enter the string:")
Upper=0
for i in range(len(str)):
    if str[i].isupper():
        Upper+=1
    else:
        continue
print(f"no of capital letters is:{Upper}")

#2.	 Count total number of vowels in a given string.
str=input("Enter a string: ")
str1=str.lower()
vowels=["a","e","i","o","u"]
num_v=0
for i in range(len(str1)):
    if str1[i] in vowels:
        num_v+=1
    else:
        continue
print(f"The number of vowels in {str1} is {num_v}")

# 3.	 Input a sentence and print words in separate lines.
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

# 4.	WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
string = input("Enter a string: ")
substring = input("Enter a sub string: ")
count = 0
start = 0
while True:
    start = string.find(substring, start) + 1
    if start > 0:
        count += 1
    else:
        break
print(count)

# 5.	Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
string = "ABaBCbGc"
counts = {}
for char in string:
    if char.isalpha():
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1
for char, count in counts.items():
    print(f"{count}{char}")
# 6.	Program to count number of unique words in a given sentence using sets.
sentence = "I am Satvik Raj studing in UPES"
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
# 7.Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#       a)	Fruits which are in both sets s1 and s2
#       b)	Fruits only in s1 but not in s2
#       c)	Count of all fruits from s1 and s2
s1 = set(input("Enter fruits in set s1 separated by space: ").split())
s2 = set(input("Enter fruits in set s2 separated by space: ").split())
common_fruits = s1.intersection(s2)
only_in_s1 = s1.difference(s2)
all_fruits = len(s1.union(s2))
print("Fruits in both sets:", common_fruits)
print("Fruits only in s1:", only_in_s1)
print("Count of all fruits from s1 and s2:", all_fruits)
# 8.	Take two sets and apply various set operations on them :
S1 = {'Red', 'yellow', 'orange', 'blue'}
S2 = {'violet', 'blue', 'purple'}
print("Intersection:", S1.intersection(S2))
print("Union:", S1.union(S2))
print("Difference (S1 - S2):", S1.difference(S2))
print("Difference (S2 - S1):", S2.difference(S1))
print("Symmetric Difference:", S1.symmetric_difference(S2))
# 1.	Scan n values in range 0-3 and print the number of times each value has occurred.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
count = [0,0,0]
if i in lst:
    if i == 0:
        count[0]+=1
    if i == 1:
        count[1]+=1
    if i == 1:
        count[2]+=1
print(f"Number of 1 = {count[0]},Number of 1 = {count[1]},Number of 2 = {count[2]}")
# 2. Create a tuple to store n numeric values and find average of all values
tp = 1,2,3,3,5,1
ave = sum(tp)/len(tp)
print("Average = ",ave)
# 3.	WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
lst.sort()
print("Runner up: ",lst[-2])
# 4. Create a dictionary of n persons where key is name and value is city. 
#   a) Display all names
#   b) Display all city names
#   c) Display student name and city of all students.
#   d) Count number of students in each city.

person_dict = {}
num_persons = int(input("Enter the number of persons: "))
for i in range(num_persons):
    name = input(f"Enter name for person {i + 1}: ")
    city = input(f"Enter city for {name}: ")
    person_dict[name] = city
print("All Names:")
for name in person_dict:
    print(name)
print("All Cities:")
unique_cities = set(person_dict.values())
for city in unique_cities:
    print(city)
print("Student Name and City:")
for name, city in person_dict.items():
    print(f"{name}: {city}")
city_counts = {}

for city in person_dict.values():
    city_counts[city] = city_counts.get(city, 0) + 1

print("Number of students in each city:")
for city, count in city_counts.items():
    print(f"{city}: {count}")
# 5.Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
#       a)	print all movie details
#       b)	display name of movies released before 2015
#       c)	print movies that made a profit.
#       d)	print movies directed by a particular director.

movies = {}
n = int(input("Enter the number of movies: "))
for i in range(n):
    name = input(f"Enter name of movie {i + 1}: ")
    year = int(input(f"Enter release year for {name}: "))
    director = input(f"Enter director name for {name}: ")
    production_cost = float(input(f"Enter production cost for {name}: "))
    collection = float(input(f"Enter collection made (earning) for {name}: "))
    movies[name] = {
        "Year": year,
        "Director": director,
        "Production Cost": production_cost,
        "Collection": collection
    }
print("\nAll Movie Details:")
for movie, details in movies.items():
    print(f"{movie}: {details}")
print("\nMovies Released Before 2015:")
for movie, details in movies.items():
    if details["Year"] < 2015:
        print(movie)
print("\nMovies That Made a Profit:")
for movie, details in movies.items():
    if details["Collection"] > details["Production Cost"]:
        print(movie)
director_name = input("\nEnter director name to filter movies: ")
print(f"\nMovies Directed by {director_name}:")
for movie, details in movies.items():
    if details["Director"].lower() == director_name.lower():
        print(movie)
# 1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  
def MinMax(ls):
    s = ls[0]
    l = ls[0]
    for i in ls:
        if i>l:
            l=i
        if i<s:
            s=i
    return s,l
ls = [1,2,3]
print(MinMax(ls))
# 2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
def sumOfCube(a):
    if a==1:
        return 1
    return (a**3)+sumOfCube(a-1)
a = int(input("Enter a positive integer: "))
print("Sum of Cubes: "+sumOfCube(a))
# 3.	Write a Python function to print 1 to n using recursion
def print1ToN(a):
    if a==1:
        print(1)
        return 0
    print1ToN(a-1)
    print(a)
    return 0
a = int(input("Enter a positive integer: "))
print1ToN(a)
# 4.	Write a recursive function to print Fibonacci series upto n terms
num = int(input("Enter number of terms: "))
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
for i in range(num):
    print(fibonacci(i),end=" ")
# 5.	Write a lambda function to find volume of cone
pi = 3.14159624
coneVolume = lambda r,h : 0.33333*r*r*h*pi
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
print("Volume of cone = ",coneVolume(r,h))
# 6.	Write a lambda function which gives tuple of max and min from a list.
ls = [1,2,4,1,7]
MinMax = lambda Nums: (max(Nums), min(Nums))
print(MinMax(ls))
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
# 1. Add few names, one name in each row, in “name.txt” file.
#       a.	Count no of names
#       b.	Count all names starting with vowel
#       c.	Find longest name

countNames = 0
countNamesStartVowel = 0
longestName = ""

with open("names.txt", "r") as f: 
    x = f.read()
    for i in x.split("\n"):
        if i:
            countNames+=1
            if i[0].upper() in ['A','E','I','O','U']:
                countNamesStartVowel+=1
            if len(longestName)<len(i):
                longestName = i
print(f'Number of Names: {countNames}\nNumber of Names starting with vowels: {countNamesStartVowel}\nLongest Name: {longestName}')
# 2. Store integers in a file.
#       a.	Find the max number
#       b.	Find average of all numbers
#       c.	Count number of numbers greater than 100
countNum = 0
countNumGT100 = 0
total = 0
with open("numbers.txt","r") as nums:
    for i in nums.read().split():
        i = int(i)
        countNum+=1
        total+=i
        if i>100:
            countNumGT100+=1
average = total/countNum
print(f"Number of Numbers: {countNum}\nNumber of Numbers Greater than 100: {countNumGT100}\nAverage of all numbers = {average}")
# 3.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM)):
#       a.	Display details of all cities
#       b.	Display city names with population more than 10Lakhs
#       c.	Display sum of areas of all cities

citiesPopGT10Lakhs = []
totalArea = 0

with open("cities.txt", "r") as f: 
    x = f.read()
    for i in x.split("\n"):
        if i:
            cl = i.split()
            print(f"""City Name: {cl[0]}
    Population: {cl[1]}
    Area: {cl[2]} sq KM""")
            totalArea += float(cl[2])
            if float(cl[1])>10:
                citiesPopGT10Lakhs.append(cl[0])
print("Cities with more than 10 Lakh people: ")
for i in citiesPopGT10Lakhs:
    print(i,end=" ")

print(f'\nTotal City area: {totalArea}')
# 4. Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError
a = input('Enter a Value: ')
b = input('Enter a Value: ')

try:
    a = int(a)
    b = int(b)
    c = a/b
    print(c)
except (ValueError, ZeroDivisionError) as E:
    print("Error:",E)
# 5. Create multiple suitable exceptions for a file handling program.
try:
    f = open("NONExistentFile",'r')
except FileNotFoundError as e:
    print("The File Does Not Exist.")
try:
    with open('writeProtectedFile.txt', 'w') as file:
        file.write("Some data")
except PermissionError:
    print("You don't have permission to write to this file.")
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
# Q1. Create numpy array to find sum of all elements in an array.
import numpy as np

Arr = np.array([1,2,3])
print(f"Sum= {sum(Arr)}")

# Q2. Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
import numpy as np

array = np.array([[5, 6, 3],[1, 9, 4],[7, 2, 8]])

row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
flattened = array.flatten()
flattened.sort()
second_max = flattened[-2]

print("Array:")
print(array)
print("Sum of rows:", row_sums)
print("Sum of columns:", column_sums)
print("Second maximum element:", second_max)

import numpy as np

A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
C = np.dot(A, B)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Result of Matrix Multiplication A * B:")
print(C)

# Q4 Write a Pandas program to get the index of an array values element-wise
import pandas as pd
data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(data)
print(df)

# Q5. Write a Pandas program to get the first 3 rows of a given DataFrame.
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
first_three_rows = df.iloc[:3]

print("First three rows of the data frame:")
print(first_three_rows)

# Q6. Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
df = pd.DataFrame(exam_data)
print("Original DataFrame:")
print(df)
df.fillna({'score':0}, inplace=True)
print("\nUpdated DataFrame:")
print(df)

# Q7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
t = np.arange(0.0, 2.0, 0.01)
s = [np.sin(i*np.pi) for i in t]
plt.subplot(2, 2, 1)
plt.plot(t, s)
plt.title('Line Plot')
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 45, 10]
# Bar Chart
plt.subplot(2, 2, 2)
bars = plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Quantity')

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(values, labels=categories)
plt.title('Pie Chart')

# Histogram
plt.subplot(2, 2, 4)
data = np.random.randn(100)
plt.hist(data, bins=10)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
