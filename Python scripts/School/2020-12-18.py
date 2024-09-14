D1 = {1:1,2:2}
D2 = {1:1,2:2,3:3}
D = {}
for key in dict2: 
    if key in dict1: 
        dict2[key] = dict2[key] + dict1[key] 
    else: 
        pass
          
print(dict2) 
print(D)