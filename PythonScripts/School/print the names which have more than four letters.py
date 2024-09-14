n = input("Enter the names seprated by space: ")
t = tuple(n.split())
for i in t:
    if len(i) > 4:
        print (i)