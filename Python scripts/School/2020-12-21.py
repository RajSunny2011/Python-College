#Q: WAP to create a dict where the elements from a list are the keys and its frequency is the value.
"""L = eval(input())
res = {}
for i in L:
    res[i] = L.count(i)"""

#HWQ: WAP to crete a dict that counts the num ber of occurences of vowels in a given string.
#The vowel is the keyword the count is the value
S = input()
Su = S.upper()
D = {}
for i in ('A','E','I','O','U'):
    D.update({i:Su.count(i)})
print(D)