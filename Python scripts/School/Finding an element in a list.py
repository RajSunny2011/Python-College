L = [11,20,3.4,79,"World","hello"]
n = input("Enter: ")
if L.count(n) >= 1 or L.count(eval(n)) >= 1:
    print("Found")
else:
    print("Not Found")