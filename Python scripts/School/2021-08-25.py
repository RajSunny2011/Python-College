#WAP (menu driven) to create a csv file to store library data(Bookid,Bookname,Authorname):
#(I)   Obtain the data from user for 5 books
#(II)  Search the csv file to a given bookName/authorName
#(III) For a book name by a given author, append the book name to the authorName and rewrite the file

import csv

def addBook():
    File = open('Library.csv','a+',newline='')
    n = int(input('Enter the number of Books: '))
    List = []
    for i in range(n):
        L = []
        a = input('Book id: ')
        L.append(a)
        a = input('Book Name: ')
        L.append(a)
        a = input('Author Name: ')
        L.append(a)
        List.append(L)
    w = csv.writer(File,delimiter=',')
    w.writerows(List)
    File.close()
    menu()

def search():
    while True:
        print("Enter 1 to Search by Book Name")
        print("Enter 2 to Search by Author Name")
        Choice =  int(input("Enter: "))
        break
    File = open('Library.csv','r')
    L = csv.reader(File)
    if Choice == 1:
        n = input("Enter Book Name: ")
        for i in L:
            if n.upper() == i[1].upper():
                print(i)
                break
    if Choice == 2:
        n = input("Enter Author Name: ")
        for i in L:
            if n.upper() == i[2].upper():
                print(i)
                break
    File.close()
    menu()


def menu():
    while True:
        print("===>Enter 1 to Add Book")
        print("===>Enter 2 to Search file")
        print("===>Enter 0 to Exit")
        choice = int(input("Enter: "))
        if choice == 1:
            addBook()
            break
        if choice == 2:
            search()
            break
        if choice == 0:
            break
menu()