L = eval(input('Enter a list: '))
LU,res = [],[]
for i in L:
    if i not in LU:
        LU.append(i)
for i in LU:
    res.append((i,L.count(i)))
print(res)