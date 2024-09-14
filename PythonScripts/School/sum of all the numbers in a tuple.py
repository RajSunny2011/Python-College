t = eval(input("Enter a tuple: "))
ts = 0
for i in t:
    if type(i) in [float,int]:
        ts += i
print(ts)