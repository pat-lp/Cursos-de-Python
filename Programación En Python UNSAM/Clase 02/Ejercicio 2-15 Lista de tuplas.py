'''
------------------------------------------------------------------------------
Ejercicio 2.15: Lista de tuplas
------------------------------------------------------------------------------
Usando este código como guía, creá un nuevo archivo informe.py. En este 
archivo, definí una función leer_camion(nombre_archivo) que abre un archivo con
el contenido de un camión, lo lee y devuelve la información como una lista 
de tuplas.
------------------------------------------------------------------------------
'''


import csv

#funcion que tiene que devolver una lista de tuplas

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
           lote = (row[0],int(row[1]),float(row[2]))
           camion.append(lote)
    return camion


camion=leer_camion("Data/camion.csv")
print(camion)

total=0.0
for s in camion:
    total+=s[1]*s[2]
    
print("Costo total nro 1: ",total)

total=0.0
for nombre,cajones,precio in camion:
    total+=cajones*precio
    
print("Costo total nro 2: ",total)