# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:30:42 2021

@author: Patricia
"""


'''
------------------------------------------------------------------------------
Ejercicio 6-05: Crear una función de alto nivel para la ejecución del programa.
------------------------------------------------------------------------------
Juntá la última parte de tu programa en una única función 
informe_camion(nombre_archivo_camion, nombre_archivo_precios). Deberías obtener 
una función que al llamarla como sigue, imprima el informe:

informe_camion('../Data/camion.csv', '../Data/precios.csv')
En su versión final tu programa será una serie de definiciones de funciones 
seguidos por un único llamado a la funcion informe_camion() (la cual ejecuta 
todos los pasos que constituyen tu programa).

Cuando tu programa es una única función, es muy simple ejecutarlo con diferentes 
entradas. Por ejemplo, después de ejecutar tu programa probá estos comandos en 
modo interactivo:
------------------------------------------------------------------------------
'''
import csv

def leer_camion(nombre_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    camion = []
    with open(nombre_archivo) as f:
        lineas = csv.reader(f)
        headers = next(lineas)

        for linea in lineas:
            record = dict(zip(headers, linea))
            cajon = {
                'nombre' : record['nombre'],
                'cajones' : int(record['cajones']),
                'precio' : float(record['precio'])
            }
            camion.append(cajon)
    return camion


def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precios ={}
    with open(nombre_archivo) as f:
        lineas = csv.reader(f)
        for linea in lineas:
            try:  
                fruta = linea[0]
                precio = float(linea[1])
                precios[fruta] = precio
                #precios[linea[0]] = float(linea[1]) otra opcion
            except:
                pass
    return precios

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def hacer_informe(camion, precios):
    listaInforme= []
    cambio=0
   
    for i in camion:
        for item in precios.items():
            if item[0]==i['nombre']:
                cambio= item[1]-i['precio']
            tabla=(i['nombre'],i['cajones'],i['precio'],round(cambio,2))
        listaInforme.append(tabla)
    return imprimir_informe(listaInforme)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    return hacer_informe(leer_camion(nombre_archivo_camion), leer_precios(nombre_archivo_precios))



informe_camion('../Data/camion.csv', '../Data/precios.csv')


files = ['../Data/camion.csv', '../Data/camion2.csv']

for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()