import pickle as pk

def addBook():
    File = open('Library.dat','ab+')
    n = int(input('Enter the number of Books: '))
    try:
        File.seek(0)
        L = pk.load(File)
    except EOFError:
        L = []
    for i in range(n):
        Lst = []
        a = input('Book id: ')
        Lst.append(a)
        a = input('Book Name: ')
        Lst.append(a)
        a = input('Author Name: ')
        Lst.append(a)
        L.append(Lst)
    File.close()
    pk.dump(L,open('Library.dat','wb'))

def search():
    while True:
        print("Enter 1 to Search by Book Name")
        print("Enter 2 to Search by Author Name")
        Choice =  int(input("Enter: "))
        break
    File = open('Library.dat','rb')
    L = pk.load(File)
    if Choice == 1:
        n = input("Enter Book Name: ")
        for i in L:
            if n.upper() == i[1].upper():
                print(f"Book id: {i[0]} \nBook Name: {i[1]}\nAuthor Name: {i[2]}")
                break
    if Choice == 2:
        n = input("Enter Author Name: ")
        for i in L:
            if n.upper() == i[2].upper() or n.upper() == i[2][0:(-1*len(i[1]))].upper():
                print(f"Book id: {i[0]} \nBook Name: {i[1]}\nAuthor Name: {i[2]}")
    File.close()

def deleteBook():
    File = open("Library.dat","rb")
    bookId = input("Enter the id: ")
    L = pk.load(File)
    for i in L:
        if i[0] == bookId:
            L.remove(i)
    File.close()
    pk.dump(L,open("Library.dat","wb"))

def mupAuthMod():
    File = open('Library.dat','rb+')
    L = pk.load(File)
    authLst = [i[2] for i in L]
    for i in range(len(authLst)):
        if authLst.count(authLst[i])>1:
            L[i][2] += L[i][1]
    File.close()
    pk.dump(L,open('Library.dat','wb'))

def read():
    File = open('Library.dat','rb')
    L = pk.load(File)
    print(L)
    File.close()

def menu():
    while True:
        print("Enter 1 to Add Book")
        print("Enter 2 to Search file")
        print("Enter 3 to Modify all authors with multiple books")
        print("Enter 4 to Read")
        print("Enter 5 to Delete a Book")
        print("Enter 0 to Exit")
        choice = int(input("Enter: "))
        if choice == 1:
            addBook()
            menu()
            break
        if choice == 2:
            search()
            menu()
            break
        if choice == 3:
            mupAuthMod()
            menu()
            break
        if choice == 4:
            read()
            menu()
            break
        if choice == 5:
            deleteBook()
            menu()
            break
        if choice == 0:
            break

menu()