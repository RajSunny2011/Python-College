def swap(a):
    n=len(a)
    k=a[n-1]
    for i in range(n-2,-1,-1):
        a[i-1]=a[i]
    a[0] = k
    return a
a = [1,2,3,4]
swap(a)
print(a)