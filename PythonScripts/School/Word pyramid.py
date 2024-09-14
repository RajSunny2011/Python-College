a = ord("0")
b = int(input("number of lines: "))
for i in range(1,b+1):
    for j in range(i):
        print(chr(a+j),end="")
    print()