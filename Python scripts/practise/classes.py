# Class defines what an object is going to be
# Classes are created using the keyword 'class' and an indented block
class MyClass:
    x = 5
    y = 75

print(MyClass().x)
print(MyClass().y)

print('='*60)

# A class can contain class methods (functions)
class Person:
    def __init__(self, name, gender, age): #The main method needs to be initialilzed with '__init__'.
        self.name = name #The self parameter needs to be written to run the current instance of the class
        self.age = age
        self.gender = gender

p1 = Person("John","M", 36) #python assigns self argument
p2 = Person("Sam","F", 14)
p3 = Person("Kim","O", 45)

print(p1.name)
print(p2.gender)
print(p3.age)

print('='*60)

# Multiple methods can be in a class
class Person:
    species = 'not a robot'
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
    def greet(self):
        print('Hello my name is '+self.name+'.')
        print('I am '+str(self.age)+' years old.')
        print('My gender is '+self.gender + '.')
        print('I am '+self.species)

p1 = Person("John","Male", 36)
p2 = Person("Sam","Female", 14)
p3 = Person("Kim","Helicopter", 745)

p3.greet()
