'''
-------------------------------------------------------------------------------
Ejercicio 3.20: Contar ejemplares por especie
-------------------------------------------------------------------------------
Usando contadores como en el Ejercicio 3.11, escribí una función 
contar_ejemplares(lista_arboles) que, dada una lista como la que generada con 
leer_parque(), devuelva un diccionario en el que las especies (recordá, es la 
columna 'nombre_com' del archivo) sean las claves y tengan como valores 
asociados la cantidad de ejemplares en esa especie en la lista dada.

Luego, combiná esta función con leer_parque() y con el método most_common() 
para informar las cinco especies más frecuentes en cada uno de los siguientes 
parques:

'GENERAL PAZ'
'ANDES, LOS'
'CENTENARIO'
-------------------------------------------------------------------------------
'''

import csv
from collections import Counter
import pprint

def leer_parque(nombre_archivo, parque):
    listaDiccionarios=[]
    with open (nombre_archivo,"rt",encoding="UTF-8") as  f:
        filas =csv.reader(f)
        encabezado=next(filas)
        
        for n_fila,fila in enumerate(filas):
            record=dict(zip(encabezado,fila))
            try:
                if record['espacio_ve'] == parque.upper():
                    d={ 'long':float(record['long']),
                        'lat': float(record['lat']),
                        'id_arbol': int(record['id_arbol']),
                        'altura_tot': int(record['altura_tot']),
                        'diametro': int(record['diametro']),
                        'inclinacio': int(record['inclinacio']),
                        'id_especie': int(record['id_especie']),
                        'nombre_com': record['nombre_com'],
                        'nombre_cie': record['nombre_cie'],
                        'tipo_folla': record['tipo_folla'],
                        'espacio_ve': record['espacio_ve'],
                        'ubicacion': record['ubicacion'],
                        'nombre_fam': record['nombre_fam'],
                        'nombre_gen': record['nombre_gen'],
                        'origen': record['origen'],
                        'coord_x': float(record['coord_x']),
                        'coord_y': float(record['coord_y'])}
                    listaDiccionarios.append(d)
            except ValueError:
                print(f"Error en la línea {n_fila+1}")
    return listaDiccionarios
 
def especies(lista_arboles):
    'Devuelve las especies de un parque'
    conjunto=set()
    for i in lista_arboles:
        conjunto.add(i['nombre_com'])
    return conjunto

def contar_ejemplares(lista_arboles):
    'Devuelve un diccionario con los nombres de las especies y la contidad de ejemplares'
    cantidad_ejemplares=Counter()
    for i in lista_arboles:
        if i['nombre_com'] in especies(lista_arboles):
           cantidad_ejemplares[i['nombre_com']] +=1
    return cantidad_ejemplares


#parque=input("Ingrese parque para saber cantidad de árboles: ")
#arbolado = leer_parque("Data/arbolado-en-espacios-verdes.csv",parque.upper())

#print("El parque '{}' tiene una lista con '{} árboles'.".format(parque.upper(),len(arbolado)))
#print("El conjunto de especies en el parque '{}' es de {} y son:\n {}".format(parque.upper(),len(especies(arbolado)),especies(arbolado)))


arbolado = leer_parque("Data/arbolado-en-espacios-verdes.csv","GENERAL PAZ")

print("El parque '{}' tiene una lista con '{} árboles'.".format("GENERAL PAZ",len(arbolado)))
print("-------------------------------------------------------------")
print("Ejemplares")
print("-------------------------------------------------------------")
pprint.pprint(contar_ejemplares(arbolado))

#%% CONTAR EJEMPLARES POR ESPECIES
'''
Luego, combiná esta función con leer_parque() y con el método most_common() para 
informar las cinco especies más frecuentes en cada uno de los siguientes parques:

'GENERAL PAZ'
'ANDES, LOS'
'CENTENARIO'
'''

def contar_ejemplares_frecuentes(nombre_archivo, parque,mas_comunes):
    'Devuelve un diccionario con los nombres de las especies y la contidad de ejemplares'
    lista_parques=leer_parque(nombre_archivo,parque)
    cantidad_ejemplares=Counter()
    for i in lista_parques:
        if i['nombre_com'] in especies(lista_parques):
           cantidad_ejemplares[i['nombre_com']] +=1
    return cantidad_ejemplares.most_common(mas_comunes)

print("-------------------------------------------------------------")
print("GENERAL PAZ")
print("-------------------------------------------------------------")

pprint.pprint(contar_ejemplares_frecuentes("Data/arbolado-en-espacios-verdes.csv","GENERAL PAZ",5))


print("-------------------------------------------------------------")
print("LOS ANDES")
print("-------------------------------------------------------------")

pprint.pprint(contar_ejemplares_frecuentes("Data/arbolado-en-espacios-verdes.csv","andes, los",5))

print("-------------------------------------------------------------")
print("CENTENARIO")
print("-------------------------------------------------------------")

pprint.pprint(contar_ejemplares_frecuentes("Data/arbolado-en-espacios-verdes.csv","Centenario",5))