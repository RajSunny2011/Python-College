import numpy as np

A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
B = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
C = np.dot(A, B)
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Result of Matrix Multiplication A * B:")
print(C)

