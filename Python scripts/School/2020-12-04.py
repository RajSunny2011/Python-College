#Q WAP to check if a tuple is in sescending order
"""t = eval(input('enter a tuple:'))
t1 = tuple(sorted(t,reverse=True))
if t == t1:
    print('Tuple is in descending order')
else:
    print('Tuple is in not descending order')"""
#Q WAP to check if the number of elments in the first half of the element is in ascending order
"""t = eval(input())
t1 = t[:len(t)//2]
if t1 == tuple(sorted(t1)):
    print("True")
else:
    print("False")"""
#Q WAP to check if there are duplicates in a tuple without using count
"""t = eval(input())
for i in range(len(t)):
    for j in t[i+1:]:
        if t[i] == j:
            print("Duplicates")
            a=1
            break
        a=0
    if a==1:
        break
if a!=1:
    print("no duplicates")"""