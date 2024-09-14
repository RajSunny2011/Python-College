a = 2
b = 0
while b < 10:
    x = 2
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            break
    else:
        print(a)
        b += 1
    a += 1