'''
-------------------------------------------------------------------------------
Ejercicio 8.7: Lectura y selección
-------------------------------------------------------------------------------
'''

import pandas as pd
import os

directorio = '../Data'
archivo =  'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_lineal = df[cols_sel]

print(df_lineal)

print()
print("Diez especies más frecuentes\n")

cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
print(cant_ejemplares.head(10))

#Se seleccionan las siguientes especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

#Forma de seleccionar
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
print()
print(df_lineal_seleccion)
