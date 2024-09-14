# Q9) Print all prime numbers between 1 and 100.
a = 2
while a < 100:
    x = 2
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            break
    else:
        print(a)
    a += 1
