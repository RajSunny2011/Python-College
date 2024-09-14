# Python gives 3 wways a txt file

# <filehandle>.read(n): will read 'n' bytes at most; if no 'n' is specified, entire file is read
# 1 byte stores 1 string character
with open('f123.txt','r') as f123:
    print(f123.read(5))

# <filehandle>.readline(n): reads one line; will read 'n' bytes at most, if specified
with open('f123.txt','r') as f123:
    print(f123.readline()) # it also reads the \n

# <filehandle>.readlines(): reads all lines and returns them in a list
with open('f123.txt','r') as f123:
    print(f123.readlines())