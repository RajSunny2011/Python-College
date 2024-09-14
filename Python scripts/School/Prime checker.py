a = int(input())
b = int(a**0.5)
for c in range (2,b+1):
    if a % c == 0:
        print("not prime")
        break
else:
    print("prime")