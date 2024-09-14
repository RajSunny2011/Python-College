#printing every character of a string in a new line
"""str = "HELLO"
for i in range (len(str)):
    print(str[i])
for i in str:
    print(i)"""

#alternating letters are upper case
a = "ululululululululululul"
b = ''
for i in range(len(a)):
    if (i % 2 == 0):
        b += a[i].upper()
    else:
        b += a[i]
print(b)