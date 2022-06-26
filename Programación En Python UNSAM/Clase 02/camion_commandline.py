'''
------------------------------------------------------------------------------
Ejercicio 2.10: Ejecución de la línea de comandos con parámetros
------------------------------------------------------------------------------
'''

import csv
import sys

def costo_camion(nombre_archivo):
    costoTotal=0
    f=open(nombre_archivo)
    rows=csv.reader(f)
    next(rows)
    for row in rows:
        try:
            costoTotal+=int(row[1])*float(row[2])
        except ValueError:
            print("Error")
    f.close()
    return costoTotal

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = ("Data/camion.csv")

costo = costo_camion(nombre_archivo)
print("\n-----------------------------")
print('Costo total:', costo) #47671.15
print("-----------------------------")


