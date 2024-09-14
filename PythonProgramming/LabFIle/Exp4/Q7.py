# Q7) Count and print all numbers divisible by 5 or 7 between 1 to 100.
divby5or7 = [num for num in range(1, 101) if num % 5 == 0 or num % 7 == 0]
print(f"Numbers divisible by 5 or 7 between 1 to 100: {divby5or7}")
print(f"Count: {len(divby5or7)}")