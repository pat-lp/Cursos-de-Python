'''
-------------------------------------------------------------------------------
Ejercicio 3.19: Determinar las especies en un parque
-------------------------------------------------------------------------------
Escribí una función especies(lista_arboles) que tome una lista de árboles como 
la generada en el ejercicio anterior y devuelva el conjunto de especies (la 
columna 'nombre_com' del archivo) que figuran en la lista.
Sugerencia: Usá el comando set como en la Sección 2.5.
-------------------------------------------------------------------------------
'''

import csv

#--------------------------3.18----------------------------

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

#--------------------------3.19----------------------------
def especies(lista_arboles):
    'Devuelve un conjunto con las especies de un parque'
    conjunto=set()
    for i in lista_arboles:
        conjunto.add(i['nombre_com'])
    return conjunto

parque=input("Ingrese parque para saber cantidad de árboles: ")
arbolado = leer_parque("Data/arbolado-en-espacios-verdes.csv",parque.upper())

print("El parque '{}' tiene una lista con '{} árboles'.".format(parque.upper(),len(arbolado)))
print("El conjunto de especies en el parque '{}' es de {} y son:\n {}".format(parque.upper(),len(especies(arbolado)),especies(arbolado)))

