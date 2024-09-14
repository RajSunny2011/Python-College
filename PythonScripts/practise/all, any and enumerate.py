nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]): #returns True only if all the cases are true
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]): #returns True if any case is true
    print("At least one is even")

for v in enumerate(nums):
    print(v)