import numpy as np
arr = np.array([1,2,3,4,5])
arrCopy = arr.copy()
arrVeiw = arr.view()
arr[0]=0
print("Original:",arr,"\nVeiw:",arrVeiw,"\nCopy:",arrCopy)
arrVeiw.base[1] = 1
print("Original:",arr,"\nVeiw:",arrVeiw,"\nCopy:",arrCopy)
