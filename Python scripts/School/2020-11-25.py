#basic functions for tuples
"""t = (1,3,4,2,5,6,1)
print(len(t))
print(t.count(1))
print(max(t))
print(min(t))"""

#inputing a tuple
"""t = eval(input())
print(t)"""

#to have a single element tuple you need to have a comma
"""t,t1,t2 = (0),(0,1),(0,)
print(type(t),type(t1),type(t2))"""

#to sum all the elements(if possible)
"""t = (1,1,1,1)
print(sum(t))"""

#to sort all the elements in a new list
t = (9,6,4,7,3,5,2,1,8,0)
l = sorted(t)
print(l)
l = tuple(l)
print(l)