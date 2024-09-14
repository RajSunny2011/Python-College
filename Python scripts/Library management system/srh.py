import pickle as pk
def search():
    try:
        File = open('Library.dat','rb+')
    except FileNotFoundError:
        print("File Not Found")
        return
    while True:
        print("Enter 1 to Search by Book Name")
        print("Enter 2 to Search by Author Name")
        Choice =  int(input("Enter: "))
        break
    L = pk.load(File)
    if Choice == 1:
        n = input("Enter Book Name: ")
        for i in L:
            if n.upper() == i[1][0:len(n)].upper():
                print('=='*20)
                print("Book id: {0}\nBook Name: {1}\nAuthor Name: {2}\n".format(*i))
                if i[3]:
                    print("Issued by "+i[3])
                else:
                    print("UNISSUED")
                print('=='*20)
    if Choice == 2:
        n = input("Enter Author Name: ")
        for i in L:
            if n.upper() == i[2][0:len(n)].upper():
                print('=='*20)
                print("Book id: {0}\nBook Name: {1}\nAuthor Name: {2}\n".format(*i))
                if i[3]:
                    print("Issued by '"+i[3]+"'")
                else:
                    print("UNISSUED")
                print('=='*20)
    File.close()