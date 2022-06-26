'''
-------------------------------------------------------------------------------
Ejercicio 4.11: Extraer datos de un archivo CSV
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''

#Primero, leamos el encabezado (header) del archivo CSV:
    
import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

print(headers) #['nombre', 'fecha', 'hora', 'cajones', 'precio']

#Luego, definamos una lista que tenga las columnas que nos importan:
    
select = ['nombre', 'cajones','precio']

#Ubiquemos los índices de esas columnas en el CSV:
    
indices = [headers.index(ncolumna) for ncolumna in select]

print(indices)#[0, 3, 4]


#Leer los datos y armar un diccionario usando 'COMPRENSIÓN DE DICCIONARIOS':

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select,indices) }

print(record) #{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}


#Comprensión de leer_camion()
camion = [ { ncolumna: row[index]  for ncolumna,index in zip(select,indices)}   for row in rows     ]

print(camion)