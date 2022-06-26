
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df =pd.read_csv(fname)
print(df)

print(pd.date_range('20200923', periods = 7))

print(pd.date_range('20200923 14:00', periods = 7))

print(pd.date_range('20200923 14:00', periods = 6, freq = 'H'))

print(pd.Series([1,2,3,4,5,6], index = pd.date_range('20200923 14:00', periods=6, freq='H')))

#%% CAMINATAS AL AZAR

import numpy as np

idx = pd.date_range('20200923 14:00', periods=120, freq='min')

s1 = pd.Series(np.random.randint(-1,2,120), index=idx)
s2 = s1.cumsum()

print(s2.plot())
 #%%
 
w=5 #ancho en minutos de la ventana
s3=s2.rolling(w).mean()
s3.plot()

#%% AMBAS CURVAS EN UN MISMO GRAFICO

df_series_23 = pd.DataFrame([s2,s3]).T #dataframe con ambas series
df_series_23.plot()