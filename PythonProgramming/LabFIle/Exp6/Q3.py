# 3.	WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
lst.sort()
print("Runner up: ",lst[-2])
