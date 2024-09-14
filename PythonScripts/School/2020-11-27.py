#Traversing a Tuple
"""T=(1,2,3,5,6,8,10)
for i in T:
    print(i,end=" ")
print()
for i in range(0,len(T)):
    print(T[i],end=" ")
print()"""

#Adding elements to a Tuple   
"""T=(1,2,3,5,6,8,10)
x=int(input("enter num: "))
T+=(x,)
print(T)
print(type(T))"""

#Modifying a Tuple - by converting to a list
T=(1,2,3,5,6,8,10)
L=list(T)
L[-2],L[-1]=40,90
T=tuple(L)
print(T)