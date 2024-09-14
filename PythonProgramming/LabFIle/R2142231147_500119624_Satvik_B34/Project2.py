import datetime
import tabulate as tab

#Searches Through 'Books.txt' for matches in books names. Takes a String input as key to search
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
            Headers = ["Book ID","Book Name","Author name","Status","Current Issuer","Date Last Issued","Other Details"]
            for book in matches:
                book[3] = Status(book[3])
            print(tab.tabulate(matches, headers=Headers, tablefmt="simple"))
        else:
            print("No Books found.")

#Takes 'bookid' input(string) and traverses through 'book.txt' for a match, if match is found then the status is set to '1' and issuer is removed
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
        if index < len(Books):
            book = Books[index].split(";")
            if book[3] == '0':
                book[3] = "1"
                book[4] = ""
                Books[index] = ";".join(book)
                print("ID: {0} Name: {1} Returned.".format(*book))
                File.seek(0)
                File.truncate(0)
                File.writelines(Books)
            else:
                print("Book Not Issued")
        else:
            print("Book not Found")

#Takes 'bookid' input(string) and traverses through 'book.txt' for a match, if match is found then the status is set to '0' and issuer is set to current user
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
        if index < len(Books):
            book = Books[index].split(";")
            if book[3]:
                book[3] = "0"
                book[4] = CurrentUser
                x = datetime.date.today()
                book[5] = x.strftime("%d-%m-%Y")
                Books[index] = ";".join(book)
                print("ID: {0}, Name: {1} Issued to {4}.".format(*book))
                File.seek(0)
                File.truncate(0)
                File.writelines(Books)
            else:
                print("Book already issued.")
        else:
            print("Book Not Found")

# displays all books in a table
def display():
    with open("Books.txt", "r") as books:
        matches = []
        Status = lambda X : "Avaiable" if X == "1" else "Not Available"
        for book in books:
            BoookDetails = book.split(";")
            BoookDetails[-1] = BoookDetails[-1].rstrip("\n")
            matches.append(BoookDetails)
        if matches:
            Headers = ["Book ID","Book Name","Author name","Status","Current Issuer","Date Last Issued","Other Details"]
            for book in matches:
                book[3] = Status(book[3])
            print(tab.tabulate(matches, headers=Headers, tablefmt="simple"))
        else:
            print("No Books found.")

#removes the book from 'books.txt'
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
            Books.pop(index)
            print("Book Deleted.")
            File.seek(0)
            File.truncate(0)
            File.writelines(Books)
        else:
            print("Book Not Found")

#adds book entry to 'books.txt'
def addBook():
    with open('Books.txt','a') as Books:
        id = input("Enter Bookid: ")
        name = input("Enter Book's Name: ")
        author = input("Enter Author's Name: ")
        other = input("Enter Other Details (sepearted by comma):")
        Books.write(f"{id};{name};{author};1;;;{other}")
        print("Entry added.")

#Modifies selected element of the given book
def modify():
    while True:
        choice = input("Enter 1 to Edit Book id\nEnter 2 to Edit Book Name\nEnter 3 to Edit Author Name\nEnter 4 to Edit Other details\nEnter 0 to Exit\nEnter: ")
        if choice == '1':
            with open("Books.txt","r+") as File:
                bookid = input("Enter the Old Book id: ")
                Books = list(File)
                index = 0
                for entry in Books:
                    if entry.split(";")[0] == bookid:
                        break
                    else:
                        index+=1
                if index < len(Books):
                    book = Books[index].split(";")
                    newbookid = input("Enter The new Book Id: ")
                    book[0] = newbookid
                    Books[index] = ";".join(book)
                    print("ID: {0} Name: {1} Updated.".format(*book))
                    File.seek(0)
                    File.truncate(0)
                    File.writelines(Books)
                else:
                    print("Book Not Found")
        elif choice == '2':
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
                    book = Books[index].split(";")
                    newbookname = input("Enter The new Book Name: ")
                    book[1] = newbookname
                    Books[index] = ";".join(book)
                    print("ID: {0} Name: {1} Updated.".format(*book))
                    File.seek(0)
                    File.truncate(0)
                    File.writelines(Books)
                else:
                    print("Book Not Found")
        elif choice == '3':
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
                    book = Books[index].split(";")
                    newBookAuth = input("Enter The new Author Name: ")
                    book[2] = newBookAuth
                    Books[index] = ";".join(book)
                    print("ID: {0} Name: {1} Author: {2} Updated.".format(*book))
                    File.seek(0)
                    File.truncate(0)
                    File.writelines(Books)
                else:
                    print("Book Not Found")
        elif choice == '4':
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
                    book = Books[index].split(";")
                    details = book[6].rstrip("\n").split(",")
                    print(f"Current Details: ")
                    for i, val in enumerate(details):
                        print (i+1, ":",val.strip(" "))
                    while True:
                        print(f"Current Details: ")
                        for i, val in enumerate(details):
                            print (i+1, ":",val.strip(" "))
                        choice = input("Enter 1 to Remove Detail\nEnter 2 to Enter Detail\nEnter 0 to Exit\nEnter: ")
                        if choice == '1':
                            pos = int(input("Enter which Detail to remove: "))
                            details.pop(pos-1)
                            book[6] = ",".join(details)+"\n"
                            Books[index] = ";".join(book)
                            File.seek(0)
                            File.truncate(0)
                            File.writelines(Books)
                        elif choice == '2':
                            det = input("Enter Detail: ")
                            details.append(det)
                            book [6] = ",".join(details)+"\n"
                            Books[index] = ";".join(book)
                            File.seek(0)
                            File.truncate(0)
                            File.writelines(Books)
                        else:
                            break
                else:
                    print("Book Not Found")
        else:
            print("Exiting...")
            break

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
        choice  = int(input("Enter 1 to login\nEnter 2 to create account\nEnter 0 to close\nEnter: "))
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
        choice = input("Enter 1 to Return\nEnter 2 to Add Books\nEnter 3 to Delete a Book\nEnter 4 to Modify a Book\nEnter 5 to Display all Books\nEnter 0 to Logout\nEnter: ")
        if choice == '1':
            returnBook()
        elif choice == '2':
            addBook()
        elif choice == '3':
            deleteBook()
        elif choice == '4':
            modify()
        elif choice == '5':
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