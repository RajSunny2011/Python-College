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
