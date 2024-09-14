D1 = {1:1,2:2}
D2 = {1:1,2:2,3:3}
D = {}
for key in D2: 
    if key in D1: 
        D2[key] = D2[key] + D1[key] 
    else: 
        pass
print(D2) 
print(D)