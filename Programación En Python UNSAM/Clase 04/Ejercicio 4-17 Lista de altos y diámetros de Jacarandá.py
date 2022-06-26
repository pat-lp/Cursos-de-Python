'''
-------------------------------------------------------------------------------
Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
-------------------------------------------------------------------------------
En el ejercicio anterior usaste una sola linea para seleccionar las alturas de 
los Jacarandás en parques porteños. Ahora te proponemos que armes una nueva 
lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino 
también el diámetro de cada Jacarandá en la lista
-------------------------------------------------------------------------------
'''

import csv 

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


arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
alturasYDiametrosArboles = alturas_y_diametros_arboles(arboleda, 'Jacarandá')
print("------------------------------------------------------------------")
print("{:^60}".format('TUPLAS CON ALTURA Y DIAMETRO DE LOS JACARANDÁS'))
print("------------------------------------------------------------------")
print(alturasYDiametrosArboles)
    
