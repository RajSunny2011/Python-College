Str = input()
result = [] 
def permute(l, i, length):  
    if i == length:
        result.append(''.join(l) )
        result.sort()
        #print ("entering if")
    else:
        #print ("entering else")
        for j in range(i, length):
            l[i], l[j] = l[j], l[i]
            #print("/",result)
            permute(l, i + 1, length)  
            l[i], l[j] = l[j], l[i]
            #print(result)
permute(list(Str), 0, len(Str)) 
print(result)
print(result.index(Str)+1)