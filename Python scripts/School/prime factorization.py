def primefactors(n):
    pl = []
    for i in range(2,n+1):
        while n % i == 0:
            pl.append(i)
            n /= i
    return(pl)
print(primefactors(8))