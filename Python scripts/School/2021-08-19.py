#Q: WAF to modifydata(rno) which modifies the name of student for the indentified roll no in student.dat (studentname, rno, percentage)
import pickle as pk
def Modifydata(rno):
    o = open('student.dat','rb+')
    r = pk.load(o)
    for i in r:
        if i[1] == rno:
            i[0] = input('Enter the new name: ')
            break
    o.seek(0)
    pk.dump(r,o)
    o.seek(0)
    print(pk.load(o))
    o.close()

x = input('Enter the roll no: ') 
Modifydata(x)