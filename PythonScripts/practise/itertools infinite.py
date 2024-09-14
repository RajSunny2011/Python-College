#following three are infinite iterators
from itertools import count #counts up from given value infinitely
from itertools import cycle #cycles given iterator infinitely
from itertools import repeat #repeats given object infinitely or given number of times
for j in count(3):
    print(j)
    if j >=11:
        break

print('='*50)

i = 0
for j in cycle('wrw'):
    if i<5:
        print(j)
        i += 1
    else:
        break

print('='*50)

for j in repeat('w',5): #the second number decides the number of repetition, taken as infinite if left blank
    print (j)