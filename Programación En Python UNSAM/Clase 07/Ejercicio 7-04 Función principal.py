'''
-------------------------------------------------------------------------------
Ejercicio 7.4: Función principal
-------------------------------------------------------------------------------
'''

import csv

def leer_camion(nombre_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    camion = []
    with open(nombre_archivo) as f:
        lineas = csv.reader(f)
        headers = next(lineas)

        for linea in lineas:
            record = dict(zip(headers, linea))
            cajon = {
                'nombre' : record['nombre'],
                'cajones' : int(record['cajones']),
                'precio' : float(record['precio'])
            }
            camion.append(cajon)
    return camion


def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    Devuelve un diccionario {nombre:precio, ...}
    '''
    precios ={}
    with open(nombre_archivo) as f:
        lineas = csv.reader(f)
        for linea in lineas:
            try:  
                precios[linea[0]] = float(linea[1]) 
            except:
                pass
    return precios

def imprimir_informe(informe):
    '''
    Da el formato de tabla para imprimir un informe conteniendo: 
        Nombre,Cajones, Precio y Cambio.
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for nombre, cajones, precio, cambio in informe:
        p=' '+'$'+str(precio)
        print(f'{nombre:>10s}{cajones:>10d}{p:>11s}{cambio:>10.2f}')


def hacer_informe(camion, precios):
    listaInforme= []
    cambio=0
   
    for i in camion:
        for item in precios.items():
            if item[0]==i['nombre']:
                cambio= item[1]-i['precio']
            tabla=(i['nombre'],i['cajones'],i['precio'],round(cambio,2))
        listaInforme.append(tabla)
    return imprimir_informe(listaInforme)

def main(archivo_camion,archivo_precios):
    '''
    Se pasa por parámetro los nombres de los archivos y se 
    genera el informe correspondiente.
    '''
    precios = leer_precios(archivo_precios)
    camion=leer_camion(archivo_camion)
    hacer_informe(camion, precios)
    print("\nFin función principal")
    

if __name__ == "__main__":
    print("Función principal")
    main('../Data/camion.csv', '../Data/precios.csv')