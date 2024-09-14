import pickle as pk
def issue():
    try:
        File = open('Library.dat','rb+')
    except FileNotFoundError:
        print("File Not Found")
        return
    L = pk.load(File)
    Book = int(input("Enter the Book id: "))
    for i in L:
        if i[0] == Book:
            Name = input("Enter the name of the Borrower: ")
            Bookn = i[1]
            confir = input("Issue '{}' to '{}'.(Y/N): ".format(Bookn,Name))
            if confir.upper() == 'Y':
                i[3] = Name
            break
    else:
        print("Book NOT FOUND")
    File.close
    pk.dump(L,open('Library.dat','wb'))