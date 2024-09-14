def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)

n = int(input("Enter an Integer: "))
print(fact(n))