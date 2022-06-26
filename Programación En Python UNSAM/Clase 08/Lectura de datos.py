
import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
print(df)

#%%

print(df.head(10))#lee las primeras 10 líneas

#%%

print(df.tail(5)) #lee las últimas 5 filas

#%% NOMBRES DE LAS COLUMNAS

print(df.columns)

#%% INDICES

print(df.index)#RangeIndex(start=0, stop=51502, step=1)

#%% DESCRIBE

print(df[['altura_tot', 'diametro', 'inclinacio']].describe())

#%% UNIQUE

#print(df['nombre_com']).unique()

#%% PREGUNTAR POR UN NOMBRE ESPECIFICO

print(df['nombre_com'] == 'Ombú')

#Se pueden usar los True para saber la cantidad
print((df['nombre_com'] == 'Ombú').sum())


#Con otras especies
cantidad_ejemplares = df['nombre_com'].value_counts()
print(cantidad_ejemplares.head(10))

#%% FILTROS BOOLEANOS

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
print(df_jacarandas)

#seleccionar columnas de interes
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
print(df_jacarandas.tail()) #imprime las últimas 5 filas, se debe realizar una copia

print(df_jacarandas.describe())

#%% REALIZAR COPIA

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
print(df_jacarandas)

#%%  SCATTERPLOTS

df_jacarandas.plot.scatter(x='diametro', y = 'altura_tot')

#%% UTILIZANDO LIBRERIA SEABORN

import seaborn as sns

sns.scatterplot(data=df_jacarandas, x='diametro', y ='altura_tot')

#%% FILTRO POR INDICE Y POR POSICION

cant_ejemplares = df['nombre_com'].value_counts()
print(cant_ejemplares.index)

print(df.loc[165])

print(cant_ejemplares.loc['Eucalipto'])

print(df_jacarandas.iloc[0])

print(cant_ejemplares.iloc[0:3])

print(df_jacarandas.iloc[-5:,2])#últimas 5 columnas y tercer columna

#%% SELECCION DE UNA COLUMNA

df_jacarandas_diam = df_jacarandas['diametro']
print(type(df_jacarandas_diam)) #Serie

print(type(df_jacarandas)) #DataFrame