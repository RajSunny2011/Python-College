#1.	 Write a program to count and display the number of capital letters in a given string.
str=input("enter the string:")
Upper=0
for i in range(len(str)):
    if str[i].isupper():
        Upper+=1
    else:
        continue
print(f"no of capital letters is:{Upper}")

#2.	 Count total number of vowels in a given string.
str=input("Enter a string: ")
str1=str.lower()
vowels=["a","e","i","o","u"]
num_v=0
for i in range(len(str1)):
    if str1[i] in vowels:
        num_v+=1
    else:
        continue
print(f"The number of vowels in {str1} is {num_v}")

# 3.	 Input a sentence and print words in separate lines.
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)

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

# 5.	Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
string = "ABaBCbGc"
counts = {}
for char in string:
    if char.isalpha():
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1
for char, count in counts.items():
    print(f"{count}{char}")
# 6.	Program to count number of unique words in a given sentence using sets.
sentence = "I am Satvik Raj studing in UPES"
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
# 7.Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#       a)	Fruits which are in both sets s1 and s2
#       b)	Fruits only in s1 but not in s2
#       c)	Count of all fruits from s1 and s2
s1 = set(input("Enter fruits in set s1 separated by space: ").split())
s2 = set(input("Enter fruits in set s2 separated by space: ").split())
common_fruits = s1.intersection(s2)
only_in_s1 = s1.difference(s2)
all_fruits = len(s1.union(s2))
print("Fruits in both sets:", common_fruits)
print("Fruits only in s1:", only_in_s1)
print("Count of all fruits from s1 and s2:", all_fruits)
# 8.	Take two sets and apply various set operations on them :
S1 = {'Red', 'yellow', 'orange', 'blue'}
S2 = {'violet', 'blue', 'purple'}
print("Intersection:", S1.intersection(S2))
print("Union:", S1.union(S2))
print("Difference (S1 - S2):", S1.difference(S2))
print("Difference (S2 - S1):", S2.difference(S1))
print("Symmetric Difference:", S1.symmetric_difference(S2))
