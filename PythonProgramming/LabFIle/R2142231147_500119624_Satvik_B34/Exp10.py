# Q1. Create numpy array to find sum of all elements in an array.
import numpy as np

Arr = np.array([1,2,3])
print(f"Sum= {sum(Arr)}")

# Q2. Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
import numpy as np

array = np.array([[5, 6, 3],[1, 9, 4],[7, 2, 8]])

row_sums = np.sum(array, axis=1)
column_sums = np.sum(array, axis=0)
flattened = array.flatten()
flattened.sort()
second_max = flattened[-2]

print("Array:")
print(array)
print("Sum of rows:", row_sums)
print("Sum of columns:", column_sums)
print("Second maximum element:", second_max)

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

# Q4 Write a Pandas program to get the index of an array values element-wise
import pandas as pd
data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
df = pd.DataFrame(data)
print(df)

# Q5. Write a Pandas program to get the first 3 rows of a given DataFrame.
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
first_three_rows = df.iloc[:3]

print("First three rows of the data frame:")
print(first_three_rows)

# Q6. Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
df = pd.DataFrame(exam_data)
print("Original DataFrame:")
print(df)
df.fillna({'score':0}, inplace=True)
print("\nUpdated DataFrame:")
print(df)

# Q7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
t = np.arange(0.0, 2.0, 0.01)
s = [np.sin(i*np.pi) for i in t]
plt.subplot(2, 2, 1)
plt.plot(t, s)
plt.title('Line Plot')
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 45, 10]
# Bar Chart
plt.subplot(2, 2, 2)
bars = plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Quantity')

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(values, labels=categories)
plt.title('Pie Chart')

# Histogram
plt.subplot(2, 2, 4)
data = np.random.randn(100)
plt.hist(data, bins=10)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
