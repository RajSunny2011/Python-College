File = open('File.txt','r+')
str = File.read()
print(type(str))
print(str)
c = 0
for cha in str:
    if cha.upper() in ['A','E','I','O','U']:
        c += 1
print('vowel count:', c)

# count the occurences of the word the in a text file
File = open('File.txt','r+')
str = File.read()
strl = str.split()
c = 0
for wrd in str:
    if wrd.upper() == 'THE':
        c += 1
print('count:', c)
