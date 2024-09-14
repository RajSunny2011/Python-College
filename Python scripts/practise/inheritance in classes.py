class Animal: # super class
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal): # sub class
    def purr(self):
        print("Purr...")
        
class Dog(Animal): # sub class
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown") # calling the sub class
print(fido.color)
fido.bark()
print('='*50)

class human: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        print("Hi! I am a human")

class lizard(human):
    def speak(self): # this method will overwrite the orginal method if the sub class is used
        print("I too am a human")

Zuckerberg = lizard("Max", "grey")
Zuckerberg.speak()

print('='*50)

# super func calls the super class
# Inheritance can happen through multiple methods
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print('THIS IS B')
        super().spam() # super func calls 'A'
    def call(self):
        print('THIS IS B TOO')

class C(B):
    def spam(self):
        print('THIS IS C')
        super().call() # super func calls 'B'
C().spam()
B().spam()