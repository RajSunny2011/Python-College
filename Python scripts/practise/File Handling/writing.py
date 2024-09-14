# <filehandle>.write(str): writes 'str' to the file
with open('hello.txt','w') as hello:
    hello.write('hello\n')

L = ['hello\n','nice to meet you\n','I am a human']
# <filehandle>.writelines(list): writes all srtings in 'list' as lines in file
with open('hello.txt','a') as hello:
    hello.writelines(L)

