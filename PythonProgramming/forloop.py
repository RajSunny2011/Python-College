a = int(input("Enter- 1 for increasing order; 2 for decreasing order: "))
if a == 1:
    for i in range(0,11,2):
        print(i)
elif a == 2:
    for i in range(10,0,-1):
        print(i)
else:
    print("Wrong Input!")