'''
-------------------------------------------------------------------------------
Ejercicio 8.8: Boxplots
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

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')