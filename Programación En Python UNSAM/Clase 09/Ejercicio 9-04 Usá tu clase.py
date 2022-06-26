'''
-------------------------------------------------------------------------------
Ejercicio 9.4: Usá tu clase
-------------------------------------------------------------------------------
Copiá los archivos informe_final.py y costo_camion.py a la carpeta de ejercicios de la clase actual. Modificá la función leer_camion() en el programa informe_final.py de modo que lea un archivo con el contenido de un camion y devuelva una lista de instancias de Lote como mostramos recién en el Ejercicio 9.3.

Cuando hayas hecho esto, cambiá un poco el código en informe_final.py y en costo_camion.py de modo que funcionen con objetos Lote (instancias de la clase Lote) en lugar de diccionarios.
-------------------------------------------------------------------------------
'''

import fileparse
import lote

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion_diccionario = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_diccionario]
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lotes in camion:
        cambio = precios[lotes['nombre']] - lotes['precio']
        t = (lotes['nombre'], lotes['cajones'], lotes['precio'], cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)



print(leer_camion('../Data/camion.csv'))
print(informe_camion('../Data/camion.csv', '../Data/precios.csv'))