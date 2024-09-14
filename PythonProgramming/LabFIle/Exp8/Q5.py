# 5. Create multiple suitable exceptions for a file handling program.
try:
    f = open("NONExistentFile",'r')
except FileNotFoundError as e:
    print("The File Does Not Exist.")
try:
    with open('writeProtectedFile.txt', 'w') as file:
        file.write("Some data")
except PermissionError :
    print("You don't have permission to write to this file.")
