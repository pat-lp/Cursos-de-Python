# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:53:05 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio 4.10: Extracción de datos
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''

import csv
import pprint

def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario, se agrega dict(zip())'
    camion = []
    f=open(nombre_archivo)
    filas = csv.reader(f)
    encabezados= next(filas)
    for n_fila,fila in enumerate(filas):
        record = dict(zip(encabezados,fila))
        try:
            lote={'nombre':record['nombre'],'cajones':int(record['cajones']),'precio':float(record['precio'])}
            camion.append(lote)
        except ValueError:
            print(f"Error en fila {n_fila}")
    f.close()
    return camion

camion = leer_camion('../Data/camion.csv')

#Lista de tuplas(nombre,cajones)

nombre_cajones = [ (s['nombre'], s['cajones']) for s in camion]
print("\nNombre de tuplas de cajones(nombre,cajones\n",nombre_cajones)


#Cambiando [] por {} se obtiene comprensión de conjuntos, con valores únicos

nombres = {  s['nombre']  for s in camion}
print("\nNombres", nombres)

# Si se especifica clave:valor se puede construir un diccionario

stock = { nombre:0 for nombre in nombres }
print("\nEjemplo de construcción de diccionario")
pprint.pprint(stock)


#Sumar cajones al diccionario anterior

for s in camion:
    stock[s['nombre']] += s['cajones']
    
print("\nDiccionario anterior con agregado de información")
pprint.pprint(stock)

#Diccionario de precios de venta

camion_precios = { nombre: precios[nombre] for nombre in nombres}

print(camion_precios)
