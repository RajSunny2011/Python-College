import pickle as pk
def display():
    try:
        File = open('Library.dat','rb')
    except FileNotFoundError:
        print("File Not Found")
        return
    L = pk.load(File)
    bl = []
    print("ISSUED:")
    for i in L:
        if i[3]:
            print("id:{0} Book: {1} by {2}  Issued by: {3}".format(*i))
        else:
            bl.append(i)
    print("Available:")
    for i in bl:
        print("id:{0} Book: {1} by {2}".format(*i))
    File.close()