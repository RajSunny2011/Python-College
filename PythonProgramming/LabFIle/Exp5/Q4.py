# 4.	WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
string = input("Enter a string: ")
substring = input("Enter a sub string: ")
count = 0
start = 0
while True:
    start = string.find(substring, start) + 1
    if start > 0:
        count += 1
    else:
        break
print(count)