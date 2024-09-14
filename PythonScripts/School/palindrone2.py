a = list(input())
a.reverse()
c = list(''.join(a))
if a == c:
    print ("palindrone")
else:
    print ("not palindrone")