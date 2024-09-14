a = input("Enter a string: ")
c = 0
d = 0
for i in a:
    i = i.lower()
    if i.isalpha():
        if i in ["a","e","i","o","u"]:
            c += 1
        else:
            d += 1
print ("Number of Vowels:",c)
print ("Number of Consonants:",d)