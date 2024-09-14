#HWQ: WAP to create a dict which counts the number of occurences the words 'THE','AN','AND', and 'OF' in a given string.
S = input()
Sl = S.upper().split()
D = {}
for i in Sl:
    if i in ('THE','AN','AND','OF'):
        D.update({i:Sl.count(i)})
print(D)