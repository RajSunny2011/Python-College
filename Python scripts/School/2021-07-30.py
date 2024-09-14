#Q: WAP to take an input from the user and write it in a file.
i = input('Enter: ')
File = open('File.txt','a+')
File.write(i)
File.close()