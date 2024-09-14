#Q. WAF to input 2 integers and return their sum
"""def sum():
    a=int(input())
    b=int(input())
    return a+b
print(sum())"""
#Q. WAF to input a number and check if the number is prime
"""def primecheck():
    a=int(input())
    isprime = 0
    for i in range(2,a):
        if a % i == 0:
            isprime = 1
            break
        else:
            isprime = 0
    return a,isprime
a,isprime = primecheck()
if isprime == 0:
    print(a,'is a prime number.')
elif isprime == 1: 
    print(a,'is a composite number.')"""
#HWQ. WAF to take an input andd check whether it is an armstrong number or not
def Armstrong():
    a=int(input('Enter a number: '))
    b=a
    s=0
    while b>0:
        d=b%10
        s+=d*d*d
        b//=10
    if a==s:
        return a,1
    else:
        return a,0
a,F=Armstrong()
if F==1:
    print(a," is an armstrong number")
elif F==0:
    print(a," is not an armstrong number") 