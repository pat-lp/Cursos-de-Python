'''
-------------------------------------------------------------------------------
Ejercicio "fileparse"
-------------------------------------------------------------------------------
'''

import csv

def parse_csv(nombre_archivo, select=None, types=None,has_headers = True):
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

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for fila in filas:
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

        else: #Si el archivo no tiene encabezados
            registros = []
            for fila in filas:
                if not fila:  # Saltear filas vacías
                    continue
                if types: #Arma tuplas ya que no hay encabezados
                    fila = tuple([func(val) for func, val in zip(types, fila)])
                registros.append(fila)
    return registros


#Función para probar lo realizado
def main():
    '''
    Función para probar lo realizado.
    '''
    precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
    return precios

#print(main())
