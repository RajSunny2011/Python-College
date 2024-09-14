f = open('sample.txt', 'r')
x = f.read()
xn = ''
for i in x:
    if i.upper() in ['A','E','I','O','U']:
        xn += i.upper()
    else:
        xn += i
f.close()

f = open('sample.txt','w')
f.write(xn)
f.close()