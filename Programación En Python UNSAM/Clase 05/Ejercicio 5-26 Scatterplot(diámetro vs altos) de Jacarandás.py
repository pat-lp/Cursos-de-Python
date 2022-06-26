'''
-------------------------------------------------------------------------------
Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
-------------------------------------------------------------------------------
En este ejercicio introducimos un nuevo tipo de gráfico: el gráfico de 
dispersión o scatterplot. El mismo usa coordenadas cartesianas para mostrar los 
valores de dos variables para un conjunto de datos.

En este caso vamos a graficar un punto en el plano (x,y) por cada árbol en el 
dataset (o para cada árbol de cierta especie). El punto correspondiente a un 
árbol con diámetro d y altura h será ubicado en la posición x=d e y=h. Este 
tipo de gráfico permite visualizar relaciones o tendencias entre las variables 
y es muy útil en el análisis exploratorio de datos.

Escribí una función scatter_hd(lista_de_pares) que a partir de una lista de 
pares como la que generaste en el Ejercicio 4.17 genere un scatterplot para 
visualizar la relación entre altura y diámetro de los Jacarandás del dataset.
------------------------------------------------------------------------------
'''

import csv 
import matplotlib.pyplot as plt
import numpy as np
import os


def  leer_arboles(nombre_archivo):
    '''Lee el archivo indicado y devuelve una lista de diccionarios con la 
     información de todos los árboles en el archivo.'''
    arboleda =[]
    with open(nombre_archivo,'rt',encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado=next(filas)
        arboleda = [{columna:indice  for columna,indice in zip(encabezado,fila)} for fila in filas]
    return arboleda

def alturas_y_diametros_arboles(arboleda,especie):
    '''lista de alturas y diámetros de los Jacarandás solamente.'''
    listaDeAlturas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas


def scatter_hd(lista_de_pares):
    array=np.array(lista_de_pares)
    plt.scatter(array[:,1], array[:,0],  c='blue', s=100,marker='x',alpha=0.2)
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.show()
    

    
arboleda = leer_arboles(os.path.join('..','Data', 'arbolado-en-espacios-verdes.csv'))
scatter_hd(alturas_y_diametros_arboles(arboleda, 'Jacarandá'))



