import pandas as pd
filepath= r"Normal-ECG.csv"
df = pd.read_csv(filepath) 
print('mean value')
print(df.mean())
print('mode')
print(df.mode())
print('maximum value')
print(df.max())
print("median value")
print(df.median())
print("standard deviation")
print(df.std())

import pandas as pd
filepath= r"Dia-ECG.csv"
df = pd.read_csv(filepath)


print('mean value')
print(df.mean())
print('mode')
print(df.mode())
print('maximum value')
print(df.max())
print("median value")
print(df.median())
print("standard deviation")
print(df.std())
