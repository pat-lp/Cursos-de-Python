'''
-------------------------------------------------------------------------------
Ejercicio 8.9: Comparando especies en parques y en veredas
-------------------------------------------------------------------------------
1-Abrí ambos datasets a los que llamaremos df_parques y df_veredas.
2-Para cada dataset armate otro seleccionando solamente las filas correspondientes 
a las tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y 
las columnas correspondientes al diametro a la altura del pecho y alturas. 
Hacelo como copias (usando .copy() como hicimos más arriba) para poder trabajar 
en estos nuevos dataframes sin modificar los dataframes grandes originales. 
Renombrá las columnas que muestran la altura y el diámetro a la altura del pecho 
para que se llamen igual en ambos dataframes, para ello explorá el comando rename.
3-Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna 
llamada 'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'.
4-Juntá ambos datasets con el comando df_tipas = pd.concat([df_tipas_veredas, 
df_tipas_parques]). De esta forma tenemos en un mismo dataframe la información 
de las tipas distinguidas por ambiente.
5-Creá un boxplot para los diámetros a la altura del pecho de la tipas distinguiendo 
los ambientes (boxplot('diametro_altura_pecho',by = 'ambiente')).
6-Repetí para alturas.
7-¿Qué tendrías que cambiar para repetir el análisis para otras especies? 
¿Convendría definir una función?
-------------------------------------------------------------------------------
'''

import pandas as pd
import os

#1-Se abren ambos datasets
directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_vereda = 'arbolado-publico-lineal-2017-2018.csv'
fname_parques = os.path.join(directorio, archivo_parques)
fname_veredas = os.path.join(directorio, archivo_vereda)

df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)

#2-Se seleccionan filas y columnas especificas
cols_parques = ['nombre_cie', 'altura_tot', 'diametro']
cols_veredas = ['nombre_cientifico', 'altura_arbol', 'diametro_altura_pecho']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols_veredas].copy()

df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho':'diametro','altura_arbol':'altura_tot'})

#3-Se agregan columnas
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'

#4-Se juntan ambos datasets
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#5-Boxplot para diametro
df_tipas.boxplot('diametro', by= 'ambiente', fontsize=5, color='green')


#6-Boxplot para altura
df_tipas.boxplot('altura_tot', by='ambiente', fontsize=5, color='violet')

#7-Para repetir el analisis para otras especies debería definir una función en la que se ingresen
#los nombres de los archivos, las especies a analizar con sus columnas correspondientes para el análisis.
#Además de los nombres de las columnas que se quieran agregar o modificar.
#Conviene hacer una función si los análisis son repetitivos para hacer más rápido el trabajo. 
