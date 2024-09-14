# Python code for printing to stderr

# importing the package
# for sys.stderr
import sys

# variables
Company = "my.org"
Location = "Noida"
Email = "my.org"

# print to stderr
print(Company, Location, Email, file=sys.stderr)