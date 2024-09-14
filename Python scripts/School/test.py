import pickle as pk
with open('pok.dat','ab+') as File:
    try:
        File.seek(0)
        L = pk.load(File)
        print(L)
    except:
        L =[]
    Lst = input()
    L.append(Lst)
    pk.dump(L,File)