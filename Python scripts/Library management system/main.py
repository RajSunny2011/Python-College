import ab,srh,detb,modify,read,issue,retbk,ds
print('='*50)
print(' '*25+"Library Management System")
def menu():
    print("Enter 1 to Issue")
    print("Enter 2 to Search")
    
    print("Enter 4 to Display all books")
    
    
    
    if choice == '1':
        issue.issue()
        menu()
    elif choice == '2':
        srh.search()
        menu()
    elif choice == '3':
        retbk.returnBook()
        menu()
    elif choice == '4':
        ds.display()
        menu()
    elif choice == '5':
        modify.modify()
        menu()
    elif choice == '6':
        ab.addBook()
        menu()
    elif choice == '7':
        detb.deleteBook()
        menu()
    elif choice == '0':
        print("="*50)
    else:
        print("Invalid input")
        menu()

menu()