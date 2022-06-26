'''
-------------------------------------------------------------------------------
Ejercicio 4.15, 4.16 y 4.17: Con archivo de arboles
-------------------------------------------------------------------------------
'''

import csv 

def  leer_arboles(nombre_archivo):
    '''Lee el archivo indicado y devuelve una lista de diccionarios con la 
     información de todos los árboles en el archivo.'''
    with open(nombre_archivo,'rt',encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado=next(filas)
        arboleda = [{ncolumna:indice  for ncolumna,indice in zip(encabezado,fila)} for fila in filas]
    return arboleda

def alturas_arboles(arboleda,especie):
    '''Lista de alturas de los Jacarandás solamente.'''
    listaDeAlturas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas


def alturas_y_diametros_arboles(arboleda,especie):
    '''Lista de alturas y diámetros de los Jacarandás solamente.'''
    listaDeAlturas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return listaDeAlturas

# Función main utilizada para imprimir y verificar los resultados obtenidos
def main():
    arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")
    alturasArboles = alturas_arboles(arboleda, 'Jacarandá')
    print("------------------------------------------------------------------")
    print("{:^60}".format('ALTURA DE LOS JACARANDÁS'))
    print("------------------------------------------------------------------")
    print(alturasArboles)
    print()
    alturasYDiametrosArboles = alturas_y_diametros_arboles(arboleda, 'Jacarandá')
    print("------------------------------------------------------------------")
    print("{:^60}".format('TUPLAS CON ALTURA Y DIAMETRO DE LOS JACARANDÁS'))
    print("------------------------------------------------------------------")
    print(alturasYDiametrosArboles)
    return "Fin función main()"
    
#print(main()) #se deja comentariada la impresión de la función