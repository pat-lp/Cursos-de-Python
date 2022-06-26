'''
-------------------------------------------------------------------------------
Ejercicio 3.21: Alturas de una especie en una lista
-------------------------------------------------------------------------------
Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista
de árboles como la anterior y una especie de árbol (un valor de la columna 
'nombre_com' del archivo), devuelva una lista con las alturas 
(columna 'altura_tot') de los ejemplares de esa especie en la lista.

Observación: Acá sí, fijate de devolver las alturas como números 
(de punto flotante) y no como cadenas de caracteres. Podés hacer esto 
modificando leer_parque.

Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en 
los tres parques mencionados.
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
 

def obtener_alturas(lista_arboles,especie):
    listaAlturas=[]
    
    for i in lista_arboles:
        if i['nombre_com']==especie:
            listaAlturas.append(i['altura_tot'])
    return listaAlturas


arboladoGP = leer_parque(archivo,"General Paz")
arboladoLA = leer_parque(archivo,"Andes, los")
arboladoCEN = leer_parque(archivo,"Centenario")


print("--------------------------------------------")
print("{:^45}".format('ALTURAS DE JACARANDÁS EN TRES PARQUES'))
print("--------------------------------------------")

print("{:>2s} {:>10s} {:>10s} {:>10s}".format('Medida','General Paz','Los Andes','Centenario'))
print("{} {:>10.2f} {:>10.2f} {:>10.2f}".format('max',max(obtener_alturas(arboladoGP, 'Jacarandá')),max(obtener_alturas(arboladoLA, 'Jacarandá')),max(obtener_alturas(arboladoCEN, 'Jacarandá'))))
print("{} {:>9.2f} {:>10.2f} {:>10.2f}".format('prom',sum(obtener_alturas(arboladoGP, 'Jacarandá'))/len(obtener_alturas(arboladoGP, 'Jacarandá')),sum(obtener_alturas(arboladoLA, 'Jacarandá'))/len(obtener_alturas(arboladoLA, 'Jacarandá')),sum(obtener_alturas(arboladoCEN, 'Jacarandá'))/len(obtener_alturas(arboladoCEN, 'Jacarandá'))))

#%% OTRA MANERA

from statistics import mean

print("--------------------------------------------")
print("{:^45}".format('ALTURAS DE JACARANDÁS EN TRES PARQUES'))
print("--------------------------------------------")

print("{:>2s} {:>10s} {:>10s} {:>10s}".format('Medida','General Paz','Los Andes','Centenario'))
print("{} {:>10.2f} {:>10.2f} {:>10.2f}".format('max',max(obtener_alturas(arboladoGP, 'Jacarandá')),max(obtener_alturas(arboladoLA, 'Jacarandá')),max(obtener_alturas(arboladoCEN, 'Jacarandá'))))
print("{} {:>9.2f} {:>10.2f} {:>10.2f}".format('prom',round(mean(obtener_alturas(arboladoGP, 'Jacarandá')),2),round(mean(obtener_alturas(arboladoLA, 'Jacarandá')),2),round(mean(obtener_alturas(arboladoCEN, 'Jacarandá')),2)))


