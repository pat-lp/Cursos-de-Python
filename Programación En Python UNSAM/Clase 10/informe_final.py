'''
-------------------------------------------------------------------------------
Ejercicio 9.8: Volvamos a armar todo
-------------------------------------------------------------------------------
Para resolver el siguiente ejercicio se utilizó el código dado por la catedra
como base.
-------------------------------------------------------------------------------
'''


import fileparse
import sys
import formato_tabla
from camion import Camion
from lote import Lote


def leer_camion(nombre_archivo):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(nombre_archivo, 'rt') as file:
        camion_dicts = fileparse.parse_csv(file, select=['nombre','cajones','precio'], types=[str,int,float])
        camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
        return Camion(camion)

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lotes in camion:
        cambio = precios[lotes.nombre] - lotes.precio
        t = (lotes.nombre, lotes.cajones, lotes.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        p = '$'+str(precio)
        rowdata = [nombre, str(cajones), f'{p}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    lista_precios = leer_precios(archivo_precios)
    precios = dict(lista_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

#%%
def f_principal(argumentos):
    if len(argumentos) == 4:
        informe_camion(argumentos[1], argumentos[2], argumentos[3])
    else:
        informe_camion(argumentos[1], argumentos[2], fmt='txt')
     

if __name__ == '__main__':
    f_principal(sys.argv)
    



