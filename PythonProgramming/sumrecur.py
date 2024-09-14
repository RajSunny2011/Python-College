def SumNNum(n):
    if n == 1:
        return 1
    return n+SumNNum(n-1)
n = int(input("Enter a Natural Number: "))
print("Sum =",SumNNum(n))