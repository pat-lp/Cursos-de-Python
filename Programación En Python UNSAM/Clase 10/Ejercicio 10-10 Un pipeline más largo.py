'''
------------------------------------------------------------------------------
Ejercicio 10.10: Un pipeline más largo
------------------------------------------------------------------------------
'''

from vigilante import vigilar
import csv

def parsear_datos(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        
        
#%% FUNCIÓN QUE ELIJA COLUMNAS ESPECÍFICAS

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0,2])
    return rows

#%% GENERADORA QUE CONVIERTE EL TIPO DE DATOS A DICCIONARIOS

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows