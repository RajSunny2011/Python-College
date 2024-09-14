import numpy as np
arr= np.array([[1,2],[4,5]])
print(arr)
print('\n')
narr = arr.reshape(-1)
print(narr)
print('\n')
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
narr = arr.reshape(4,3)#2d array
print(narr)
print('\n')
narr = arr.reshape(3,2,2)#3d array
print(narr)
print('\n')
narr = arr.reshape(1,6,2)#3d array
print(narr)
