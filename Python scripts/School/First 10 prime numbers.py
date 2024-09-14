a = 2
b = 0
while b < 10:
    x = 2
    for i in range(2, a):
        if a % x != 0:
            x += 1
    if x == a:
        print (a)
        b += 1
    a += 1