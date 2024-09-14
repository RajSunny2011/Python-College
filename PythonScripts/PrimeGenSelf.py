def primegen(n):
    primes = [2]
    for i in range(3, n+1):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

p = primegen(100000)
print(p)