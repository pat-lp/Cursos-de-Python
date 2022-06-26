'''
-------------------------------------------------------------------------------
Ejercicio 7.3: Errores silenciados
-------------------------------------------------------------------------------
'''
import csv

def parse_csv(nombre_archivo, select=None, types=None,has_headers = True,silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, 
    que debe ser una lista de nombres de las columnas a considerar.
    Crea tuplas en lugar de diccionarios cuando no hay encabezados.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
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
                        # Armar el diccionario
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
                if types: #Arma tuplas ya que no hay encabezados
                    fila = tuple([func(val) for func, val in zip(types, fila)])
                registros.append(fila)
        
    return registros



camion = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors =True)
print(camion)
