'''
------------------------------------------------------------------------------
Ejercicio 10.12: El pipeline ensamblado
------------------------------------------------------------------------------
'''



import csv
import informe_final
from formato_tabla import crear_formateador
from vigilante import vigilar

'''
def elegir_columnas(rows, indices): #sacar
    for row in rows:
        yield [row[index] for index in indices]'''
        
'''
def cambiar_tipo(rows, types): #sacar
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]'''

'''
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))'''

def parsear_datos(lines):
    rows = csv.reader(lines)
    
    #Expresion generadora reemplaza a elegir_columnas
    rows = ((row[index] for index in [0, 1, 2]) for row in rows) #elegir_columnas
    
    #Expresion generadora reemplaza a cambiar_tipo
    rows =( (func(val) for func,val in zip([str, float, int],row))for row in rows) 

    #Expresion generadora reemplaza a hace_dicts
    rows = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in rows)
    return rows


'''
def filtrar_datos(rows, nombres): #sacar
    for row in rows:
        if row['nombre'] in nombres:
            yield row'''
            
    
def ticker(camion_file, log_file, fmt):
    '''
    Crea un indicador en tiempo real para un camión, archivo log, 
    y formato de tabla de salida pasado por parámetro.
    '''
    formateador = crear_formateador(fmt)
    camion = informe_final.leer_camion(camion_file)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    rows = parsear_datos (vigilar(log_file))
    
    #Expresion generadora reemplaza a filtrar_datos
    rows = (row for row in rows if row['nombre'] in camion) 

    while True:
        for fila in rows:
            formateador.fila(str(contenido) for contenido in fila.values())
          

def f_principal():
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')

if __name__ == '__main__':
    f_principal()
    




