#sets are data structures simillar to lists and tuples
#they differ in the case that they are not ordered (no indcies) and cannot contain the same element twice
num_set = {1, 2, 3, 4, 5} #formed by curly brackets or
word_set = set(["spam", "eggs", "sausage"])#set() func
empty_set = set()#needs to be used to create an empty set because '{}' will create a dict
print(3 in num_set)
print("spam" not in word_set)

print('='*50)
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) #notice there is only one '1'
nums.add(-7) #to add a value
print(nums)
nums.remove(3) #to remove a value
print(nums)

print('='*50)
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #A union B
print(first & second) #A intersection B
print(first - second) #A-B
print(second - first) #B-A
print(first ^ second) #A union B - A intersecion B