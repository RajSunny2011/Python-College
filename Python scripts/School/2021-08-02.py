#Q: WAP to create a txt file with 5 names in seperated by new line character
names = open('names.txt','w')
for i in range(5):
    n = input('Enter name: ')
    names.write(n+'\n')
names.close()