# 1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  
def MinMax(ls):
    s = ls[0]
    l = ls[0]
    for i in ls:
        if i>l:
            l=i
        if i<s:
            s=i
    return s,l
ls = [1,2,3]
print(MinMax(ls))
