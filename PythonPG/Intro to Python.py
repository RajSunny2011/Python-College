
#Variables

x = 12 #initialize a variable called x
print(x)

y = 13 #initialize a variable called y
print (y)

print ("sum of x and y is",x+y)

#Different types of variables allowed in Python

# Integer variables can take only round numbers, both positive and negative

age = 12 # an integer variable
print (age)

# Numeric varialbes can take all real number values. Also knows as floating variables

pi = 3.1416
print (pi)

# string variables can input text. string variables must be put between quotes

name = "Barry"
print (name) # check to see what the output would be if the name isn't in quotes

#Boolean variables, They take a binary value of True or False. True and False 
#Python is case sensitive and True and False are special keywords reserved for boolean
is_complete = False

#The following program lets you input values for first_name and last_name and output the full name

#first_name = input("First Name: ") # input function helps take input from the user.
l#ast_name = input("Last Nmae: ")

#name = first_name + " " +last_name

#print("Name = ", name)

# complex numbers can be input as complex variables
 c = 4+5j # c is a complex variable with real component 4 and an imaginary component 5
 
 # j is the square root of negative 1 (-1), These have applications in engineering problems
 d = c**2 # would return the square of the complex number 4+5j
 print(d)

# operators
# Mathematical operators

z = x+y # Addition
print(z)

z = x-y # subtraction
print(z)

z = x*y  # Multiplication
print(z)

z = x/y # division
print(z)

z = x**y # exponent
print(z)

z = x%y # modulus
print(z)


# Comparison operators
# comparison operators compare values on both sides and return a True or False statement
# They are extensively used for making decisions in flowcharts, conditional statements

z = x>y # greater than operator, returns True if x is greater than y
print(z)

z = x<y # less than operator, returns False if x is less than y
print(z)

#Equality operator, Equality operators are used to check for specific values

if x==12:
    print ("x= 12") # the code checks for value of x and if it is 12, prints the value.
    
#inequality operator, inequality operator is the opposite of equality operator
    
if x!=13:
    print ("x is not equal to 13")
    
#greater than or equal to operator
    
if x>= 6:
    print ("x is greater than 6")
    
#less than or equal to operator
    
if x<= 20:
    print ("x is less than 20")

#Assignment operators
#Addition, subtraction and mulitplication can be done within the line as follows
    
x+= 4 # the value of 4 is added to x and the value is stored into the variable. 

#So, in this case, value of x should be updated to 16
 
print (x)

# same logic applies to subtraction and multiplication

x-= 4       # 4 would be subtracted and saved in x, so, the value must return to 12
print (x)

x*= 4
print (x)   # 4 would be multiplied to value of x, so, the returned value would be 48

# The same can be extended to division, modulus and exponent
# using /=, %=, **= the same can be achieved

# logical operators

#And operator, compares the logical values of the variables and returns true if the values are equal
# Returns a false value if the values are not equal. Python is case sensitive. 

a = True
b = False

# True is returned when both a and b are true or both a and b are false
print (a and b) # Returned value would be false

# or operator returns a true if atleast one of the variables is a true

print(a or b) 

print (not a)



# non primitive data types such as Lists, Tuples and Dictionary

# List
#Lists can take multipe values of different data types. Think of them as rows or records in a data set
#Lists can be intialized by using an ordered set of values between [].

list1 = [2,3,5,7,11,13,17,19,23] # list containing the first 9 prime numbers
print(list1)

list2 = ["Mercury", "Venus", "Earth", "Mars"] # list of the names of rocky planets, list of strings
print(list2)

list3 = ["lift off", "in", 5,4,3,2,1, "lift off"] # list consisting of a mix of strings and numeric variables
print(list3)

# indexing in lists. values of a list can be retrieved by mentioning their address. 
# address of a value is it's position in the list starting with 0

list3[1] # will return the second value in the list3 which is "in"

# to access multiple values from a list, a new list must be defined

# values can only be retreived one at a time. to retrieve multiple values, iterations must be used.

b = [1,3,5]
c = [list3[i] for i in b]
print(c) # returns the second, fourth and sixth values in list3. Loops will be discussed later in the exercise

# values can also be retrieved in other ways. 

print ("The first, second and third elements in list3 are: ", list3[0], list3[1], list3[2])

# values can also be retrived as vector

print(list3[1:3]) # returns the values of second, third and fourth values

#Dictionary
#Dictionaries allow defining of key value pairs. 
#Dictionaries are defined using the curly brackets {}

band = {"james" : "guitar", "kirk":"guitar", "jason":"bass", "lars":"drums"}
print(band)

#keys of the dictionary can be retrieved using the keys() function

keys = list(band.keys())
print(keys)             # Returns the list of keys

#values can be retrieved using the values() function
values = list(band.values())
print (values)

# keys and values can be checked for in a dictionary

check = "dave" in band
print("Is dave in the band:", check) # returns a true or false value

check = "james" in band
print("is james in the band:", check) # returns a true or false value


#all values of the dictionary can be erased using clear function
band.clear()
print(band) # returns an empty dictionary


#==============================================================================#
#==============================================================================#


#Conditional statements

#if else statement

x=12
y=13

if x>y:                         # if statement :
    print ("x is greater than y") #indentation happens automatically in python. 
else:                           #else :
    print("x is not greater than y")
    
# nested if else statements

if x>y:
    print ("x is greater than y")
elif x==y:
    print ("x is equal to y")
else:
    print ("x is less than y")
    
# Loops
    
# for loop

list = [1,2,3,4,5,6,7,8,9,10] # initialize a list

for i in list: # i is the variable we define which will iterate over the sequence list.
                # variable can be anything but conventionally, i is used for integers and x for string
                # initialization of the variable is done within the for loop and ends when the loop ends
    print(i*19) # returns the multiplication table for 19
    
#for loop can also be used by itself
    
for i in range(10): # when range is defined this way, the count starts from 0
    print (i)
    
for i in range(12,23): # when range is given a starting and ending value.
    print(i)
    
for i in range(20,10,-1): # when a range has to be defined in the reverse order, suggest by using a third parameter, -1
    print(i)

student = ["mark", "rob", "tom", "kevin"]

for name in student:
    print("student name: ", name)
    

# while loop
# while loops are similar to for loops but are used when observing a condition.
# while loops continues to execute the program until the condition is true 
    
count = 10

while (count >0): # checks for the value of count
    print ("the count is: ", count) # executes the task
    count = count -1 # body of the program. when count become zero, the while loop is exited

print("lift off")


# break statement
# break statements are used to exit a program when a particular criterion is met
# best used when the exit has to happen on a particular trigger.

for letter in "apocalypse":
    if letter == "y":
        break
    else:
        print (letter) # the program should print a, p, o, c, a and l and when y is encountered, it breaks
        

# continue statement
# continue statement skips the criterion and continues till the end of the program
# similar to break statement excpet that the program continues till the end
        
for letter in "apocalypse":
    if letter == "y":
        continue
    else:
        print (letter) # will print all the letters and skip over y


#=================================================================================#
#=================================================================================#
        
# Functions
# functions are defined when a complex task has to be calculated and called many times
# functions are defined using the keyword def followed by the body of the code

def hypotenuse(x,y):    # we are defining a function to calculate the hypotenuse of a triangle when the two sides are given
                    # x and y are the parameters of this function, the two sides we input
    import math      # math library contains the function sqrt() which we will be using in our custom defined function
    h = (x**2) +(y**2)
    h = math.sqrt(h)
    return h          # value of the hypotenuse is returned by invoking the function

hyp = hypotenuse(3,4)   # hyp now contains the value for the hypotenuse of a triangle with sides 3 and 4
print(hyp)

hyp = hypotenuse(5,12)
print(hyp)

