file=open("Sample2.txt","r")
x=file.read().split()
print(x)
the=0
a=0
an=0
for i in x :
    if i in ['the']:
        the+=1
    elif i in ['an']:
        a+=1
    elif i in ['this']:
        an+=1
print("'the' Count :",the)
print("'an' Count :",a)
print("'this' Count :",an)
file.close()
