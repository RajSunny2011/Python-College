from itertools import permutations
a = input()
b = list(a)
perm = permutations(b)
print ([x for x in perm])