'''
-------------------------------------------------------------------------------
Ejercicio 4.15: Lectura de todos los árboles
-------------------------------------------------------------------------------
Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, 
escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y 
devuelva una lista de diccionarios con la información de todos los árboles en 
el archivo. La función debe devolver una lista conteniendo un diccionario por 
cada árbol con todos los datos.

Vamos a llamar arboleda a esta lista.
-------------------------------------------------------------------------------
'''

import csv
import pprint

def  leer_arboles(nombre_archivo):
    '''Lee el archivo indicado y devuelve una lista de diccionarios con la 
     información de todos los árboles en el archivo.'''
    arboleda =[]
    with open(nombre_archivo,'rt',encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado=next(filas)
        arboleda = [{columna:indice  for columna,indice in zip(encabezado,fila)} for fila in filas]
    return arboleda

arbolado = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

print("------------------------------------------------------------------")
print("{:^60}".format('ARBOLADO'))
print("------------------------------------------------------------------")
pprint.pprint(arbolado)