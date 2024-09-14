import pickle as pk
v = 12
def addBook():
    File = open('Library.dat','ab+')
    n = int(input('Enter the number of Books: '))
    try:
        File.seek(0)
        L = pk.load(File)
    except:
        L = []
    for i in range(n):
        Lst = []
        try:
            Lst.append(int(L[len(L)-1][0])+1)
        except IndexError:
            Lst.append(1)
        a = input('Book Name: ')
        Lst.append(a)
        a = input('Author Name: ')
        Lst.append(a)
        Lst.append('')
        L.append(Lst)
    File.close()
    pk.dump(L,open('Library.dat','wb'))