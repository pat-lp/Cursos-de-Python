'''
-------------------------------------------------------------------------------
Ejercicio 8.10
-------------------------------------------------------------------------------
uscá los valores de delta_t (es un número entero, son pasos) y delta_h (puede 
tener decimales, es un float) que hacen que los dos gráficos se vean lo más 
similares posible.
-------------------------------------------------------------------------------
'''

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

#Se trabaja con una copia del fragmento
dh = df['12-25-2014':].copy()

#print(dh.describe())

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 19.48 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()




