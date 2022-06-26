'''
-------------------------------------------------------------------------------
Ejercicio 5.25: Histograma de altos de Jacarandás
-------------------------------------------------------------------------------
Generá un histograma con las alturas de los Jacarandás en el dataset.
-------------------------------------------------------------------------------
'''

import csv 
import os
import matplotlib.pyplot as plt


def  leer_arboles(nombre_archivo):
    '''Lee el archivo indicado y devuelve una lista de diccionarios con la 
     información de todos los árboles en el archivo.'''
    arboleda =[]
    with open(nombre_archivo,'rt',encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado=next(filas)
        arboleda = [{columna:indice  for columna,indice in zip(encabezado,fila)} for fila in filas]
    return arboleda

def alturas_arboles(arboleda,especie):
    '''lista de alturas de los Jacarandás solamente.'''
    listaDeAlturas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas



os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
plt.hist(altos,bins=25,color='green',edgecolor = 'black')
plt.title('"HISTOGRAMA DE ALTOS DE JACARANDÁS"')
plt.xlabel("Altura Jacarandás")
plt.ylabel("Cantidad de Jacarandás")
plt.show()
#plt.clf()

