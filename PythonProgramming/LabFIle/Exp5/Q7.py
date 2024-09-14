# 7.Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#       a)	Fruits which are in both sets s1 and s2
#       b)	Fruits only in s1 but not in s2
#       c)	Count of all fruits from s1 and s2
s1 = set(input("Enter fruits in set s1 separated by space: ").split())
s2 = set(input("Enter fruits in set s2 separated by space: ").split())
common_fruits = s1.intersection(s2)
only_in_s1 = s1.difference(s2)
all_fruits = len(s1.union(s2))
print("Fruits in both sets:", common_fruits)
print("Fruits only in s1:", only_in_s1)
print("Count of all fruits from s1 and s2:", all_fruits)
