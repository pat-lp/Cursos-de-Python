'''
-------------------------------------------------------------------------------
Ejercicio 3.22: Inclinaciones por especie de una lista
-------------------------------------------------------------------------------
Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada 
una especie de árbol y una lista de árboles como la anterior, devuelva una 
lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa 
especie.
-------------------------------------------------------------------------------
'''

import csv

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


print("La lista con las inclinaciones de la especie Jacarandá es:",obtener_inclinaciones(leer_parque(archivo,'general paz'), 'Jacarandá'))