
'''
Ejemplo: 12 personas caminando 8 horas
'''
import pandas as pd
import numpy as np

horas = 8
idx = pd.date_range('20200923 14:00', periods= horas*60, freq='min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks =pd.DataFrame(np.random.randint(-1,2,[horas*60, 12]).cumsum(axis=0), index = idx)

df_walks.plot()

#Suavizar lineas

w=45
df_walks_suav = df_walks.rolling(w, min_periods =1).mean()

nsuav = ['S_' + n for n in nombres]
df_walks_suav.columns = nsuav

df_walks_suav.plot()

#Guardar datos

df_walks_suav.to_csv('caminata_doce_personas_ocho_horas.csv')