#Q.write a python script to convert vowels to uppercase
"""a = input()
c = ""
for i in a:
    if i in ("a","e","i","o","u"):
        c += i.upper()
    else:
        c += i
print(c)"""
#Q.write a python script to count the occurrences of 't'or'T' and repace it with y.
a = input()
c = ""
cn = 0
for i in a:
    if i in ("T","t"):
        cn += 1
        c += 'y'
    else:
        c += i
print("count:",cn)
print(c)