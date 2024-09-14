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
