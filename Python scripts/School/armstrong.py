j = input()
k = 0
for i in j:
    l = int(i)
    k = l**3 + k
if k == int(j):
    print (j,"is an armstrong number")
else:
    print (j,"is not an armstrong number")