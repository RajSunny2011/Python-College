import pickle as pk

prices = {}

def Menu():
    print("Enter 1 to ")
    print("Enter 2 to ")
    print("Enter 3 to ")
    print("Enter 4 to ")
    print("Enter 5 to ")
    print("Enter 6 to ")
    print("Enter 0 to exit")
    mnch = input("Enter your choice: ")
    if mnch == '1':
        AddSales()
        Menu()
    if mnch == '2':
        WeekSales()
        Menu()
    if mnch == '3':
        WeekRvn()
        Menu()
    if mnch == '4':
        RmvItem()
        Menu()
    if mnch == '5':
        AddItem()
        Menu()
    if mnch ==''
    if mnch == '0':
        return

def AddSales():
    