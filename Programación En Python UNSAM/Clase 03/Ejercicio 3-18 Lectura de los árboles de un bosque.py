'''
-------------------------------------------------------------------------------
Ejercicio 3.18: Lectura de los árboles de un bosque
-------------------------------------------------------------------------------
Definí una función leer_parque(nombre_archivo, parque) que abra el archivo 
indicado y devuelva una lista de diccionarios con la información del parque 
especificado. La función debe devolver, en una lista un diccionario con todos 
los datos por cada árbol del parque elegido (recordá que cada fila del csv es 
un árbol).

Sugerencia: basate en la función leer_camion() y usá también el comando zip 
como hiciste en el Ejercicio 3.9 para combinar el encabezado del archivo con 
los datos de cada fila. Inicialmente no te preocupes por los tipos de datos de 
cada columna, pero cuando empieces a operar con una columna modificá esta 
función para que ese dato sea del tipo adecuado para operar.

Observación: La columna que indica el nombre del parque en el que se encuentra
 el árbol se llama 'espacio_ve' en el archivo CSV.

Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo, debería 
darte una lista con 690 árboles.
-------------------------------------------------------------------------------
'''

import csv

def leer_parque(nombre_archivo, parque):
    listaDiccionarios=[]
    with open(nombre_archivo, 'rt', encoding='UTF-8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        
        for n_fila, fila in enumerate(filas):
            record = dict(zip(encabezado, fila))
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



parque=input("Ingrese parque para saber cantidad de árboles: ")
arbolado = leer_parque("../Data/arbolado-en-espacios-verdes.csv",parque)


print("El parque '{}' tiene una lista con '{} árboles'.".format(parque.upper(),len(arbolado)))

