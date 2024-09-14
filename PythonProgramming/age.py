ages = [5,10,12,18,34,24,11,40]
# adults = []
# for i in ages:
#     if i>=18:
#         adults.append(i)
def adultcheck(x):
    return x>=18
adults = list(filter(adultcheck, ages))
print(adults)