'''
-------------------------------------------------------------------------------
Ejercicio 7.7: Arreglemos las funciones existentes
-------------------------------------------------------------------------------
'''

import fileparse

def leer_camion(nombre_archivo):
    '''
    Lee una cadena de lotes en un camión
    Precondición: Lee un archivo de lotes en un camión 
    Poscondición: Devuelve como lista de diccionarios con claves
    nombre, cajones, precio.
    '''
    with open(nombre_archivo) as file:
        camion=fileparse.parse_csv(file, types = [str,int,float])
    return camion

def leer_precios(nombre_archivo):
    '''
    lee precios de un objeto de dos columnas
    Precondición: La primera columna debe contener un nombre y la segunda un precio.
    Poscondición: Devuelve un diccionario {nombre:precio, ...}
    '''
    precios={}
    with open(nombre_archivo) as file:
        linea=fileparse.parse_csv(file, types =[str,float],has_headers=False)
        precios[linea[0][0]]=float(linea[0][1])
        return precios


def imprimir_informe(informe):
    '''
    Da el formato de tabla para imprimir un informe conteniendo: 
        Nombre,Cajones, Precio y Cambio.
    Precondición: Recibe la información generada en la función hacer_informe.
    Poscondición: Devuelve la impresión del informe en formato de tabla.
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for nombre, cajones, precio, cambio in informe:
        p=' '+'$'+str(precio)
        print(f'{nombre:>10s}{cajones:>10d}{p:>11s}{cambio:>10.2f}')


def hacer_informe(camion, precios):
    '''
    Función que realiza un informe.
    Precondición: Recibe dos archivos(camión y precios) para poder realizar el informe
    Poscondición: Devuelve los calculos correspondientes a los cajones según el precio.
    '''
    listaInforme= []
    cambio=0
   
    for i in camion:
        for item in precios.items():
            if item[0]==i['nombre']:
                cambio= item[1]-i['precio']
            tabla=(i['nombre'],i['cajones'],i['precio'],round(cambio,2))
        listaInforme.append(tabla)
    return imprimir_informe(listaInforme)

def f_principal(archivo_camion,archivo_precios):
    '''
    Se pasa por parámetro los nombres de los archivos y se 
    genera el informe correspondiente.
    '''
    precios = leer_precios(archivo_precios)
    camion=leer_camion(archivo_camion)
    hacer_informe(camion, precios)

    

if __name__ == "__main__":
    print("Función principal\n")
    f_principal('../Data/camion.csv', '../Data/precios.csv')