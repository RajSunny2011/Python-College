ls = [[1],[1,1]]
for i in range(1,10):
    l = [1]
    for j in range(1,len(ls[i])):
        l.insert(j,(ls[i][j-1]+ls[i][j]))
    l.append(1)
    ls.append(l)
for i in ls:
    print(i)