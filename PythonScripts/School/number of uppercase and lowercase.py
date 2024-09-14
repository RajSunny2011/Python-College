s = input("Enter a string: ")
upcount,lowcount = 0,0
for i in s:
    if i.isupper():
        upcount += 1
    elif i.islower():
        lowcount += 1
print ("number of uppercase letters:",upcount)
print ("number of lowercase letters:",lowcount)