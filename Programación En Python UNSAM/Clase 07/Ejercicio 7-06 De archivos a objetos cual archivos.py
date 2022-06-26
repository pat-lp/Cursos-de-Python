'''
-------------------------------------------------------------------------------
Ejercicio 7.6: De archivos a "objetos cual archivos"
-------------------------------------------------------------------------------
'''

import csv
import gzip


def parse_csv(lines, select=None, types=None,has_headers = True,silence_errors = True):
    '''
    Función que pasa archivos a "objetos cual archivos"
    Precondición: recibe objeto iterable que se comporte como archivo con tipado str,int,float.
    Poscondición:
        - Lista de diccionarios con las filas si tienen encabezado.
        - Tuplas en lugar de diccionarios cuando no hay encabezados.
    '''
 
    filas = csv.reader(lines)
    if has_headers: #Si el archivo tiene encabezado
        encabezados = next(filas) # Lee los encabezados del archivo
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for i,fila in enumerate(filas):
            if silence_errors == True:
                try:
                    if not fila:    # Saltear filas vacías
                        continue
                        # Filtrar la fila si se especificaron columnas
                    if indices:
                        fila = [fila[index] for index in indices]
                        # Armar el diccionario
                    if types:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
                except ValueError:
                    pass
            else:
                try:
                    if not fila:    # Saltear filas vacías
                        continue
                        # Filtrar la fila si se especificaron columnas
                    if indices:
                            fila = [fila[index] for index in indices]
                        # Arma diccionario
                    if types:
                        fila = [func(val) for func, val in zip(types, fila) ]
                        registro = dict(zip(encabezados, fila))
                except ValueError as  e:
                    print(f"Fila {i+1}: No pude convertir {fila}")
                    print(f"Fila {i+1}: Motivo:", e)
                registros.append(registro)
                        
    else: #Si el archivo no tiene encabezados
        registros = []
        for fila in filas:
            if not fila:  # Saltear filas vacías
                continue
            if types: 
                fila = tuple([func(val) for func, val in zip(types, fila)])
            registros.append(fila)
    return registros


camion = parse_csv('../Data/missing.csv', types = [str, int, float])
print("Ojo!!\n",camion) #OJO!! LA SALIDA ES UN LÍO!!
print()
with gzip.open('../Data/camion.csv.gz', 'rt') as file:
    camion = parse_csv(file, types = [str,int,float])
    print(camion)
    
    
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion =parse_csv(lines, types=[str,int,float])
print(camion)
    