import pickle as pk
def deleteBook():
    try:
        File = open('Library.dat','rb+')
    except FileNotFoundError:
        print("File Not Found")
        return
    bookId = input("Enter the id: ")
    L = pk.load(File)
    for i in L:
        if i[0] == bookId:
            ch = input("do you want ot remove {}(Y/N)".format(i[1]))
            if ch.upper() == 'Y':
                L.remove(i)
    File.close()
    pk.dump(L,open("Library.dat","wb"))