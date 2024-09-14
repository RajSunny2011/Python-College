# 5.	Write a lambda function to find volume of cone
pi = 3.14159624
coneVolume = lambda r,h : 0.33333*r*r*h*pi
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
print(coneVolume(r,h))