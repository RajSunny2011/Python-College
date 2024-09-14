# Q3) Print Fibonacci series up to given term.
term = int(input("Enter the number of terms for Fibonacci series: "))
series = [0, 1]
while len(series) < term:
    series.append(series[-1] + series[-2])
print(f"Fibonacci series up to {term} terms: {series[:term]}")
