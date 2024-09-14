# Q:
File = open('File.txt','r')
File.read(10)
print(File.tell())
File.seek(0)
line = ' '
while line:
    line = File.readline()
    print(line)

# Q:WAP to:
#   a. create a new file 'Diary.txt' and add user content
#   b. read the file and display its content
#   c. read and display lines starting with 'he','she','i' or 'you (anyone)
#   d. read and display the number of vowels and consonants
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