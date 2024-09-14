Diary = open('Diary.txt','a')
a = input('Enter: ')+'\n'
Diary.write(a)
Diary.close()

Diary = open('Diary.txt','r')
r = Diary.read()
print(r)
Diary.seek(0)

for i in Diary.readlines():
    if i[0].upper() == 'HE':
        print(i)
Diary.seek(0)

Countv = 0
Countc = 0

for i in r:
    if i.isalpha:
        if i.upper() in ['A','E','I','O','U']:
            Countv += 1
        else:
            Countc += 1

print('Number of vowels =', Countv,'\n'+'Number of consonants:',Countc)
Diary.close()