# WAP to check Prime Number
# X = int(input("Enter a Integer: "))
# for i in range(2,int(X**0.5)+1):
#     if X%i == 0:
#         print(f"{X} is not a Prime Number.")
#         break
# else:
#     print(f"{X} is a Prime Number")


# WAP to convert Decimal to Binary, Octal, Hexadecimal
# X = int(input("Enter a Integer: "))
# print(f"Binary = {bin(X).lstrip("0b")}")
# print(f"Octal = {oct(X).lstrip("0o")}")
# print(f"Hexadecimal = {hex(X).lstrip("0x")}")


# WAP to solve Quadratic equation
# A = float(input("Enter the component of x^2: "))
# if (A == 0):
#     print("The equation is not a quadratic equation.")
#     quit()
# B = float(input("Enter the component of x: "))
# C = float(input("Enter the 'C' component: "))
# D = B*B - 4*A*C
# if D>0:
#     r1 = (-B + D**0.5)/(2*A)
#     r2 = (-B - D**0.5)/(2*A)
#     print(f"Roots are: {round(r1,4)},{round(r2,4)}")
# elif D==0:
#     r = -B/(2*A)
#     print(f"Both roots are equal: {round(r,4)}")
# else:
#     print(f"Roots are Imaginary.")


# WAP to count occurences of each word in each sentence
# X = input("Enter a sentence: ")
# X = X.split(" ")
# count = {}
# for i in X:
#     s = i.strip().upper()
#     if (s in count.keys()):
#         count[s] += 1
#     else:
#         count[s] = 1
# for key, val in count.items():
#     print(f"{key}: {val}")


# WAP to create a dictionary with cricket players names, role, and scores
# players = {}
# n = int(input("Enter Number of players: "))
# for i in range(n):
#     name = input("Enter Name: ").upper()
#     role = input("Enter Role: ").upper()
#     score = int(input("Enter score of the player: "))
#     players[name] = [role,score]
# for key, val in players.items():
#     print(f"Name: {key}\n  Role: {val[0]}\n  Score: {val[1]}")
