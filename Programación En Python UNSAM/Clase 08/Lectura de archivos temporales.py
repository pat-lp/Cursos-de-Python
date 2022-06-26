'''
-------------------------------------------------------------------------------
Lectura de archivos temporales
-------------------------------------------------------------------------------
'''

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv')
print(df.head())

print(df.index)

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col =['Time'], parse_dates=True)

print(df.head())
print(df['1-18-2014 9:00' : '1-18-2014 18:00'])

print(df['2-19-2014'])#formato EEUU
print(df['12-25-2014'])

#df['12-25-2014':].plot()

df['10-15-2014' : '12-15-2014'].plot()