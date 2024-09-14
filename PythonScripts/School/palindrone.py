Num = int(input("Enter Numbe: "))
Rev = 0
Copy = Num
while Copy >0:
    Digit = Copy %10
    Rev =Rev *10 +Digit
    Copy //=10

print(Rev)
if (Rev == Num):
    print("Number is a palindrome")
else:
    print("Not a palindrome")