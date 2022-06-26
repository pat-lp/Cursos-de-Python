'''
-------------------------------------------------------------------------------
Ejercicio 5.27: Scatterplot para diferentes especies
-------------------------------------------------------------------------------
Comenzando con éste código, hacé tres gráficos como en el ejercicio anterior, 
uno por cada especie.
------------------------------------------------------------------------------
'''

import os
import matplotlib.pyplot as plt
import csv 
import numpy as np


def  leer_arboles(nombre_archivo):
    '''Lee el archivo indicado y devuelve una lista de diccionarios con la 
     información de todos los árboles en el archivo.'''
    arboleda =[]
    with open(nombre_archivo,'rt',encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado=next(filas)
        arboleda = [{columna:indice  for columna,indice in zip(encabezado,fila)} for fila in filas]
    return arboleda

#RESUELTO EN CLASE
def medidas_de_especies(especies,arboleda):
    '''Recibe una lista de nombres de especies y una lista de arboleda y 
    devuelve un diccionario.'''
    diccionario={especie: [(float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == especie]for especie in especies}
    return diccionario

#se usa os.path.join para reemplazar la "/" según sistema operativo donde se corra.
arboleda = leer_arboles(os.path.join('..','Data', 'arbolado-en-espacios-verdes.csv'))
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

def scatter_eucalipto(lista_de_pares):
    array=np.array(medidas['Eucalipto'])
    plt.scatter(array[:,1], array[:,0], color='orange',s=100,marker='x',alpha = 0.8)
    plt.title("Relación diámetro-alto para Eucaliptos")
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,130) 
    plt.ylim(0,40)
    plt.show()
    

def scatter_palo(lista_de_pares):
    array = np.array(medidas["Palo borracho rosado"])
    plt.scatter(array[:,1], array[:,0], color='green',s=100,marker='x',alpha = 0.5)
    plt.title("Relación diámetro-alto para Palo borracho rosado")
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,130) 
    plt.ylim(0,40)
    plt.show()

def scatter_jacaranda(lista_de_pares):
    array = np.array(medidas["Jacarandá"])
    plt.scatter(array[:,1], array[:,0], color='blue',s=100,marker='x',alpha = 0.5)
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.xlim(0,130) 
    plt.ylim(0,40)
    plt.show()
    

scatter_eucalipto(medidas_de_especies(especies,arboleda))
scatter_jacaranda(medidas_de_especies(especies,arboleda))
scatter_palo(medidas_de_especies(especies,arboleda))


