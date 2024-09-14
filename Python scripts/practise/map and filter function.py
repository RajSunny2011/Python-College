def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) #map func takes the value from the list and uses that as the arg for the mentioned func and adds the returned value to the list
print(result)

def even_check(x):
    return x % 2 == 0
    
nums = [11,22,33,44,55]
res = list(filter(even_check, nums)) #filter func returns the value from the list if the output of a boolean func is true
print(res)