import pickle as pk
def returnBook():
    File = open("Library.dat","rb+")
    book = int(input("Enter the Book id: "))
    L = pk.load(File)
    for i in L:
        if i[0] == book:
            print("Returning {} from {}".format(i[1],i[3]))
            i[3] = ''
            break
    else:
        print("Book NOT FOUND")
    File.close()
    pk.dump(L,open('Library.dat','wb'))
    