'''
------------------------------------------------------------------------------
Ejercicio 2.18: Balances
------------------------------------------------------------------------------
Supongamos que los precios en camion.csv son los precios pagados al productor 
de frutas mientras que los precios en precios.csv son los precios de venta en 
el lugar de descarga del camión.

Calcular el balance del negocio: calcule lo que costó el camión, lo que se 
recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa 
debe imprimir por pantalla un balance con estos datos.
------------------------------------------------------------------------------
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

def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for i,row in enumerate(rows):
        try:  
            diccionarioFrutas[row[0]] = float(row[1])
        except IndexError:
            print("Error en la línea",i+1)
    f.close()
    return diccionarioFrutas

precio=leer_precios("../Data/precios.csv")
print(precio)