import datetime
import tabulate

def search():
    with open("Books.txt", "r") as books:
        key = input("Enter the name: ")
        booklist = list(books)
        matches = []
        Status = lambda X : "Avaiable" if X == "1" else "Not Available"
        for book in booklist:
            BoookDetails = book.split(";")
            if BoookDetails[1].upper().find(key.upper()) != -1:
                matches.append(BoookDetails)
        if matches:
            print("Book ID\tBook name\t\tAuthor name\tStatus\tCurrent Issuer\tDate last Issued\tOther Details")
            for book in matches:
                print(f"{book[0]}\t{book[1]}\t{book[2]}\t{Status(book[3])}\t{book[4]}\t{book[5]}\t{book[6]}")
        else:
            print("No Books found.")

def returnBook():
    with open("Books.txt","r+") as File:
        bookid = input("Enter the Book id: ")
        Books = list(File)
        index = 0
        for entry in Books:
            if entry.split(";")[0] == bookid:
                break
            else:
                index+=1
        book = Books[index].split(";")
        if index < len(Books):
            if book[3] == '0':
                book[3] = "1"
                book[4] = ""
                Books[index] = ";".join(book)
                print("ID: {0} Name: {1} Returned.".format(*book))
                File.seek(0)
                File.truncate()
                File.writelines(Books)
            else:
                print("Book Not Issued")
        else:
            print("Book not Found")

def issue():
    global CurrentUser
    with open("Books.txt","r+") as File:
        bookid = input("Enter the book id: ")
        Books = list(File)
        index = 0
        for entry in Books:
            if entry.split(";")[0] == bookid:
                break
            else:
                index+=1
        book = Books[index].split(";")
        if index < len(Books):
            if book[3]:
                book[3] = "0"
                book[4] = CurrentUser
                x = datetime.date.today()
                book[5] = x.strftime("%d-%m-%Y")
                Books[index] = ";".join(book)
                print("ID: {0}, Name: {1} Issued to {4}.".format(*book))
                File.seek(0)
                File.truncate()
                File.writelines(Books)
            else:
                print("Book already issued.")
        else:
            print("Book Not Found")

def display():
    with open("Books.txt", "r") as books:
        matches = []
        Status = lambda X : "Avaiable" if X == "1" else "Not Available"
        for book in books:
            BoookDetails = book.split(";")
            BoookDetails[-1] = BoookDetails[-1].rstrip("\n")
            matches.append(BoookDetails)
        if matches:
            print("Book ID\tBook name\t\tAuthor name\tStatus\tCurrent Issuer\tDate last Issued\tOther Details")
            for book in matches:
                print(f"{book[0]}\t{book[1]}\t\t{book[2]}\t{Status(book[3])}\t{book[4]}\t{book[5]}\t{book[6]}")
        else:
            print("No Books found.")

def deleteBook():
    with open("Books.txt","r+") as File:
        bookid = input("Enter the Book id: ")
        Books = list(File)
        index = 0
        for entry in Books:
            if entry.split(";")[0] == bookid:
                break
            else:
                index+=1
        if index < len(Books):
            Books = Books.pop(index)
            print("Book Deleted.")
            File.seek(0)
            File.truncate()
            File.writelines(Books)
        else:
            print("Book Not Found")

def addBook():
    with open('Books.txt','a') as Books:
        id = input("Enter Bookid: ")
        name = input("Enter Book's Name: ")
        author = input("Enter Author's Name: ")
        other = input("Enter Other Details (sepearted by comma):")
        Books.write(f"{id};{name};{author};0;;;{other}")
        print("Entry added.")

def loginMenu():
    try:
        file = open("Books.txt","r")
        file.close()
    except FileNotFoundError:
        choice = input("'Books.txt' not found\nPress 1 to create empty 'Books.txt'\nPress 0 to close\nEnter: ")
        if choice == "1":
            file = open("Books.txt","w")
            file.close()
        else:
            quit()
    try:
        file = open("Users.txt","r")
        file.close()
    except FileNotFoundError:
        choice = input("'Users.txt' not found\nPress 1 to create empty 'Users.txt'\nPress 0 to close\nEnter: ")
        if choice == "1":
            file = open("Users.txt","w")
            adPassword = input("Set an Admin Password: ")
            file.write(f"Admin;{adPassword};0,0,0\n")
            file.close()
        else:
            quit()
    global CurrentUser
    while True:
        print("Enter 1 to login")
        print("Enter 2 to create account")
        print("Enter 0 to close")
        choice  = int(input("Enter: "))
        if choice == 1: 
            CurrentUser = login()
            if CurrentUser == "Admin":
                adminMenu()
            elif CurrentUser == -3:
                print("Password does not match")
            elif CurrentUser:
                userMenu()
            else:
                print("Enter correct username or create account.")
        elif choice == 2:
            res = createAccount()
            if res == 1:
                continue
            elif res == 0:
                print("User Already Exists")
            elif res == -1:
                print("Username too short.")
            elif res == -2:
                print("Password too short")
        elif choice == 0:
            print("="*50)
            break

def adminMenu():
    global CurrentUser
    while True:
        choice = input("Enter 1 to Return\nEnter 2 to Add Books\nEnter 3 to Delete a Book\nEnter 4 to Display all Books\nEnter 0 to Exit\nEnter: ")
        if choice == '1':
            returnBook()
        elif choice == '2':
            addBook()
        elif choice == '3':
            deleteBook()
        elif choice == '4':
            display()
        elif choice == '0':
            CurrentUser = ""
            break

def userMenu():
    global CurrentUser
    while True:
        choice = input("Enter 1 to Issue\nEnter 2 to Search\nEnter 3 to Display all books\nEnter 0 to Logout\nEnter: ")
        if choice == '1':
            issue()
        elif choice == '2':
            search()
        elif choice == '3':
            display()
        elif choice == '0':
            CurrentUser = ""
            break
        else:
            print("Invalid input")


def createAccount():
    with open("Users.txt","r") as Users:
        users = list(Users)
    with open("Users.txt","a") as  Users:
        user = input("Enter UserName: ")
        if len(user)<3:
            return -1
        if user in users: 
            print("User already exists.")
            return 0
        password = input("Enter Password: ")
        if len(password) < 8:
            return -2
        repassword = input("Enter Password Again: ")
        if password == repassword:
            Users.write(f"{user};{password};0,0,0\n")
            return 1
        else:
            return -3
            

def login():
    with open("Users.txt","r") as Users:
        user = input("Enter UserName: ")
        for i in Users:
            il = i.rstrip("\n").split(";")
            if user == il[0]:
                password = input("Enter Password: ")
                if password == il[1]:
                    return user
                else: 
                    print("Wrong Password!")
                    return login()
        print("User Not found!")
        return 0

print('='*50)
print(' '*12+"Library Management System")
CurrentUser = ""
loginMenu()