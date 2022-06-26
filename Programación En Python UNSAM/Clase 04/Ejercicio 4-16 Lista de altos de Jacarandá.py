'''
-------------------------------------------------------------------------------
Ejercicio 4.16: Lista de altos de Jacarandá
-------------------------------------------------------------------------------
Usando comprensión de listas y la variable arboleda podés por ejemplo armar la 
lista de la altura de los árboles.

H=[float(arbol['altura_tot']) for arbol in arboleda]
Usá los filtros (recordá la Sección 4.3) para armar la lista de alturas de los 
Jacarandás solamente.
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

def alturas_arboles(arboleda,especie):
    '''lista de alturas de los Jacarandás solamente.'''
    listaDeAlturas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
alturaArboles = alturas_arboles(arboleda, 'Jacarandá')
print("------------------------------------------------------------------")
print("{:^60}".format('ALTURA DE LOS JACARANDÁS'))
print("------------------------------------------------------------------")
print(alturaArboles)
    



