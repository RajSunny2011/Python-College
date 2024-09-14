#1.	 Write a program to count and display the number of capital letters in a given string.
str=input("enter the string:")
Upper=0
for i in range(len(str)):
    if str[i].isupper():
        Upper+=1
    else:
        continue
print(f"no of capital letters is:{Upper}")
