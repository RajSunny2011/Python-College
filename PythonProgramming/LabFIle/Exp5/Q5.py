# 5.	Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
string = "ABaBCbGc"
counts = {}
for char in string:
    if char.isalpha():
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1
for char, count in counts.items():
    print(f"{count}{char}")
    