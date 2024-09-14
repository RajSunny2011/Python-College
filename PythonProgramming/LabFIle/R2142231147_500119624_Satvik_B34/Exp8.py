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
# 2. Store integers in a file.
#       a.	Find the max number
#       b.	Find average of all numbers
#       c.	Count number of numbers greater than 100
countNum = 0
countNumGT100 = 0
total = 0
with open("numbers.txt","r") as nums:
    for i in nums.read().split():
        i = int(i)
        countNum+=1
        total+=i
        if i>100:
            countNumGT100+=1
average = total/countNum
print(f"Number of Numbers: {countNum}\nNumber of Numbers Greater than 100: {countNumGT100}\nAverage of all numbers = {average}")
# 3.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM)):
#       a.	Display details of all cities
#       b.	Display city names with population more than 10Lakhs
#       c.	Display sum of areas of all cities

citiesPopGT10Lakhs = []
totalArea = 0

with open("cities.txt", "r") as f: 
    x = f.read()
    for i in x.split("\n"):
        if i:
            cl = i.split()
            print(f"""City Name: {cl[0]}
    Population: {cl[1]}
    Area: {cl[2]} sq KM""")
            totalArea += float(cl[2])
            if float(cl[1])>10:
                citiesPopGT10Lakhs.append(cl[0])
print("Cities with more than 10 Lakh people: ")
for i in citiesPopGT10Lakhs:
    print(i,end=" ")

print(f'\nTotal City area: {totalArea}')
# 4. Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError
a = input('Enter a Value: ')
b = input('Enter a Value: ')

try:
    a = int(a)
    b = int(b)
    c = a/b
    print(c)
except (ValueError, ZeroDivisionError) as E:
    print("Error:",E)
# 5. Create multiple suitable exceptions for a file handling program.
try:
    f = open("NONExistentFile",'r')
except FileNotFoundError as e:
    print("The File Does Not Exist.")
try:
    with open('writeProtectedFile.txt', 'w') as file:
        file.write("Some data")
except PermissionError:
    print("You don't have permission to write to this file.")
