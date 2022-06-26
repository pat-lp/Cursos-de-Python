# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 17:31:51 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio "arboles"
-------------------------------------------------------------------------------
'''

import csv 
import matplotlib.pyplot as plt
import numpy as np


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
    
#Función para probar lo realizado
def main():
    arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    scatter_hd(alturas_y_diametros_arboles(arboleda, 'Jacarandá'))
    return "Fin función main()"

#print(main())