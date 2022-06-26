'''
-------------------------------------------------------------------------------
Ejercicio 4.18: Diccionario con medidas
-------------------------------------------------------------------------------
Te pedimos que armes un diccionario en el que estas especies sean las claves y
los valores asociados sean los datos que generaste en el ejercicio anterior. 
Más aún, organizá tu código dentro de una función 
medidas_de_especies(especies,arboleda) que recibe una lista de nombres de 
especies y una lista como la del Ejercicio 4.15 y devuelve un diccionario cuyas 
claves son estas especies y sus valores asociados sean las medidas generadas en 
el ejercicio anterior.

Vamos a usar esta función la semana próxima. A modo de control, si llamás a la 
función con las tres especies del ejemplo como parámetro 
(['Eucalipto', 'Palo borracho rosado', 'Jacarandá']) y la arboleda entera, 
deberías recibir un diccionario con tres entradas (una por especie), cada una 
con una lista asociada conteniendo 4112, 3150 y 3255 pares de números 
(altos y diámetros), respectivamente.
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


def alturas_y_diametros_arboles(arboleda,especie):
    '''lista de alturas y diámetros de los Jacarandás solamente.'''
    listaDeAlturas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas

#RESUELTO EN CLASE
def medidas_de_especies(especies,arboleda):
    '''Recibe una lista de nombres de especies y una lista de arboleda y 
    devuelve un diccionario.'''
    diccionario={especie: [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == especie]for especie in especies}
    return diccionario

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

    
especies=['Eucalipto','Palo borracho rosado','Jacarandá']

m=medidas_de_especies(especies, arboleda)
print("DICCIONARIO\n",m)
