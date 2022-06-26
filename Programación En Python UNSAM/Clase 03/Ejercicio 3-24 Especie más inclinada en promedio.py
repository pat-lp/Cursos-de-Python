'''
-------------------------------------------------------------------------------
Ejercicio 3.24: Especie más inclinada en promedio
-------------------------------------------------------------------------------
Volvé a combinar las funciones anteriores para escribir la función 
especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles 
devuelva la especie que en promedio tiene la mayor inclinación y el promedio 
calculado..

Resultados. Deberías obtener, por ejemplo, que los Álamos Plateados del 
Parque Los Andes tiene un promedio de inclinación de 25 grados.

Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un 
ejemplar más inclinado de toda la ciudad y no solo de un parque? ¿Podrías dar 
la latitud y longitud de ese ejemplar? ¿Y dónde se encuentra (lat,lon) el 
ejemplar más alto? ¿De qué especie es?.
-------------------------------------------------------------------------------
'''

import csv
from collections import Counter
from statistics import mean

archivo="Data/arbolado-en-espacios-verdes.csv"

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


def obtener_inclinaciones(lista_arboles, especie):
    listaInclinaciones=[]
    for i in lista_arboles:
        if i['nombre_com'] == especie:
            listaInclinaciones.append(i['inclinacio']) 
    return listaInclinaciones


def especies(lista_arboles):
    'Devuelve un conjunto con las especies de un parque'
    conjunto=set()
    for i in lista_arboles:
        conjunto.add(i['nombre_com'])
    return conjunto

def especimen_mas_inclinado(lista_arboles):
    inclinacion={}
    especie=especies(lista_arboles)
    for i in especie:
       inclinacion[i]=max(obtener_inclinaciones(lista_arboles, i))
    especimen=Counter(inclinacion).most_common(1)
    return especimen


def especie_promedio_mas_inclinada(lista_arboles):
     'Devuelve la especie que en promedio tiene la mayor inclinación y su promedio'''
     inclinacion={}
     especie=especies(lista_arboles)
     for i in especie:
         inclinacion[i]=mean(obtener_inclinaciones(lista_arboles, i))
     especimen=Counter(inclinacion).most_common(1)
     return especimen


arboladoGP = leer_parque(archivo,"General Paz")
arboladoLA = leer_parque(archivo,"Andes, los")
arboladoCEN = leer_parque(archivo,"Centenario")


print("------------------------------------------------------------")
print("{:2}".format('ESPECIE CON PROMEDIO DE INCLINACIÓN MÁS ALTO EN TRES PARQUES'))
print("------------------------------------------------------------")
print(f'GRAL. PAZ:  {especie_promedio_mas_inclinada(arboladoGP)}\nLOS ANDES:  {especie_promedio_mas_inclinada(arboladoLA)}\nCENTENARIO: {especie_promedio_mas_inclinada(arboladoCEN)}')

#GRAL. PAZ:  ('No Determinable', 25)
#LOS ANDES:  ('Álamo plateado', 25)
#CENTENARIO: ('Rosa de Siria', 25)