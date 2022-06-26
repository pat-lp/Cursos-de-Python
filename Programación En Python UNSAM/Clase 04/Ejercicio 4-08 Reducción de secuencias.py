'''
-------------------------------------------------------------------------------
Ejercicio 4.08: Reducción de secuencias
-------------------------------------------------------------------------------
Calculá el costo total de la carga del camión en un solo comando.
-------------------------------------------------------------------------------
'''

import csv


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


def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for row in rows:
        try:  
            diccionarioFrutas[row[0]] = float(row[1])
        except IndexError:
            print("Error en una línea")
    f.close()
    return diccionarioFrutas


camion=leer_camion("../Data/fecha_camion.csv")

# Usando una sola línea de código se calcula el costo del camión
costo = sum([ s['cajones'] * s['precio']   for s in camion])
print("Costo camión",costo)#47671.15

#Valor en el mercado de la carga del camión usando una sola línea de código
precios = leer_precios('../Data/precios.csv')
valor = sum([ s['cajones']* precios[s['nombre']]  for s in camion ])
print("Valor venta", valor)#62986.1


#A lo largo de la lista

print([ s['cajones'] * s['precio'] for s in camion ])

#Con sum() se realiza una reducción del resultado
#sum([ s['cajones'] * s['precio']   for s in camion])