mylist = ["Apple","Banana","Cherry","Banana"]
if "Apple" in mylist:
    print("Yes")
print(mylist)
mylist.append("Cereal")
print(mylist)
mylist.insert(1,"Milk")
print(mylist)
mylist.remove("Banana")
print(mylist)
a = mylist.pop()
print("Item Deleted: ",a)
print(mylist)
mylist[1:4] = ["Mango"]
print(mylist)
