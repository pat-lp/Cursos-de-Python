# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:11:58 2021

@author: Patricia
"""

'''
-------------------------------------------------------------------------------
Ejercicio 3.13: Recolectar datos
-------------------------------------------------------------------------------
En el Ejercicio 2.18, escribiste un programa llamado informe.py que calculaba 
las ganancias o pérdidas de un camión que compra a productores y vende en el 
mercado. Copiá su contenido en un archivo tabla_informe.py. En este ejercicio,
vas a comenzar a modificar tabla_informe.py para producir una tabla 
En este informe, el "Precio" es el precio en el mercado y el "Cambio" es la 
variación respecto al precio cobrado por el productor.

-------------------------------------------------------------------------------
'''

import csv


def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario'
    camion = []
    f=open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        diccionario = {'nombre':row[0], 'cajones':int(row[1]), 'precio': float(row[2])}
        camion.append(diccionario)
    return camion


def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for row in rows:
        try:  
            fruta = row[0]
            precio = float(row[1])
            diccionarioFrutas[fruta] = precio
        except:
            pass
    return diccionarioFrutas

precios = leer_precios('../Data/precios.csv')
print(precios)
camion=leer_camion("Data/camion.csv")

total=0.0
venta=0.0

for s in camion:
    total+=s['cajones']*s['precio']
    if precios[s['nombre']] !=0:
        venta+=precios[s['nombre']]*s['cajones']


print("---------------------------------------")
print("Costo del camión: {}\nVenta en el negocio: {}\nBalance: {}".format(total,venta,round(venta-total,2)))
print("---------------------------------------")

#%%


def hacer_informe(camion, precios):
    listaInforme= []
    cambio=0
    for i in camion:
        print(i['nombre'])
        for item in precios.items():
            print(item[0])
            if item[0]==i['nombre']:
                cambio= item[1]-i['precio']
            tabla=(i['nombre'],i['cajones'],i['precio'],round(cambio,2))
        listaInforme.append(tabla)
    return listaInforme

camion = leer_camion('../Data/camion.csv')

precios = leer_precios('../Data/precios.csv')
print(precios)

informe = hacer_informe(camion, precios)
print("--------------------------------------------------------")
print("Informe")
print("--------------------------------------------------------")
for r in informe:
    print(r)
print("--------------------------------------------------------")
