'''
-------------------------------------------------------------------------------
Ejercicio 3.23: Especie con el ejemplar más inclinado
-------------------------------------------------------------------------------
Combinando la función especies() con obtener_inclinaciones() escribí una 
función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles 
devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

Correlo para los tres parques mencionados anteriormente.

Resultados. Deberías obtener, por ejemplo, que en el Parque Centenario hay un 
Falso Guayabo inclinado 80 grados.
-------------------------------------------------------------------------------
'''

import csv
from collections import Counter

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


arboladoGP = leer_parque(archivo,"General Paz")
arboladoLA = leer_parque(archivo,"Andes, los")
arboladoCEN = leer_parque(archivo,"Centenario")

print("------------------------------------------------------------------------")
print("{:^70}".format('ESPECIMEN MÁS INCLINADO EN TRES PARQUES'))
print("------------------------------------------------------------------------")
print(f'GRAL. PAZ:  {especimen_mas_inclinado(arboladoGP)}\nLOS ANDES:  {especimen_mas_inclinado(arboladoLA)}\nCENTENARIO: {especimen_mas_inclinado(arboladoCEN)}')

#GRAL. PAZ:  [('Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)', 70)]
#LOS ANDES:  [('Jacarandá', 30)]
#CENTENARIO: [('Falso Guayabo (Guayaba del Brasil)', 80)]