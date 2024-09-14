with open("test.txt","r") as a:
    for i in a:
        print(i.rstrip("\n").split(";"))
# with open("test.txt","a") as t:
#     t.write("bye;bye\n")
with open("test.txt","r+") as a:
    ls = list(a)
    l = ls[0].split(";")
    l[1] = ""
    ls[0] = ";".join(l)
    a.seek(0)
    a.truncate()
    a.writelines(ls)