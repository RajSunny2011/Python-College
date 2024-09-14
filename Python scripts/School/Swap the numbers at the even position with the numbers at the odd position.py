l = eval(input('Enter a list: '))
l1 = []
j = 1
for i in l[::2]:
    l1.insert(j,i)
    j += 2
k = 0
for i in l[1::2]:
    l1.insert(k,i)
    k += 2
print(l1)