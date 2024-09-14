# 4.	Write a recursive function to print Fibonacci series upto n terms
num = int(input("Enter number of terms: "))
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)
for i in range(num):
    print(fibonacci(i),end=" ")