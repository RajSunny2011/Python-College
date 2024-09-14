import pickle as pk
def modify():
    File = open('Library.dat','rb+')
    L = pk.load(File)
    bookId = input("Enter book id: ")
    print("Enter 1 to edit the book name")
    print("Enter 2 to edit the author name")
    ch = input("Enter: ")
    for i in range(len(L)):
        if L[i][0] == bookId:
            if ch == '1':
                L[i][1] = input("Enter new book name: ")
                break
            if ch == '2':
                L[i][2] = input("Enter new author's name: ")
    File.seek(0)
    pk.dump(L,File)
    File.close()