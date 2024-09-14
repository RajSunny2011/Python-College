# 1.	Scan n values in range 0-3 and print the number of times each value has occurred.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
count = [0,0,0]
if i in lst:
    if i == 0:
        count[0]+=1
    if i == 1:
        count[1]+=1
    if i == 1:
        count[2]+=1
print(f"Number of 1 = {count[0]},Number of 1 = {count[1]},Number of 2 = {count[2]}")
