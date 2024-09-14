#list manupilation del {list}[]
"""lst=[4,1,4,1,4,1,4,7,5]
del lst[1:6:2]
print(lst)"""
#Q.write a program to count no. of elements in a list without using .len().
"""lst = [1,3,4,5,2]
a = 0
for i in lst:
    a += 1
print(a)"""
#Q.write a program to count no. of times a element occurs without using .count().
"""lst = [5,17,9,17,4,2,17]
a = 0
b = 17
for i in lst:
    if i == b:
        a += 1
print(a)"""
#Q.write a program to find the max value and check if it lies in the first or the second half of the list:
lst = [1,4,6,56,42,32,4]
a = max(lst)
l = len(lst)//2
if len(lst) % 2 != 0 and lst.index(a) + 1 == l:
    print("middle")
elif a in lst[:l]:
    print ("first half")
elif a in lst[l:]:
    print ("second half")