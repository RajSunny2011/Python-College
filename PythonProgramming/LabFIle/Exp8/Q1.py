# 1. Add few names, one name in each row, in “name.txt” file.
#       a.	Count no of names
#       b.	Count all names starting with vowel
#       c.	Find longest name

countNames = 0
countNamesStartVowel = 0
longestName = ""

with open("names.txt", "r") as f: 
    x = f.read()
    for i in x.split("\n"):
        if i:
            countNames+=1
            if i[0].upper() in ['A','E','I','O','U']:
                countNamesStartVowel+=1
            if len(longestName)<len(i):
                longestName = i
print(f'Number of Names: {countNames}\nNumber of Names starting with vowels: {countNamesStartVowel}\nLongest Name: {longestName}')
