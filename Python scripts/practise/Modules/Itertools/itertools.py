from itertools import takewhile #similar to filter but stops after the first False
from itertools import chain #combines two iterables in to one 
from itertools import accumulate #adds the value of sum previous iterations to the current one

i = list(takewhile(lambda x: x < 10, [1,2,34,53,3,6])) #only 1,2 will get put in the list
print (i) #because 34 < 10 returns false stopping the funtion
print(list(filter(lambda x: x < 10, [1,2,34,53,3,6]))) #1,2,3,6 gets printed

print("="*50)

l = [1,2,3]
w = 'pqow'
for j in chain(l,w):
    print(j,type(j)) #prints objects from both l and w

print('='*50)

print (list(accumulate(range(9))))

print (list(accumulate([23,42,53])))

print (list(accumulate('pop'))) #works on most iretrable objects