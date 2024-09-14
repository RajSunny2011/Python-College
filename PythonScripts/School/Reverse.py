Num = int(input("Enter Number: "))
Rev = 0
Copy = Num
while Copy > 0:
    Digit = Copy%10
    Rev = Rev*10+Digit
    Copy //= 10
print("Reverse:",Rev)