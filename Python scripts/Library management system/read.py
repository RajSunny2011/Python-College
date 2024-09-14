import pickle as pk
def read():
    File = open('Library.dat','rb')
    print(pk.load(File))
    File.close()