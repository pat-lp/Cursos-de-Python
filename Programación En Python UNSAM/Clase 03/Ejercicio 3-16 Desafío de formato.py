'''
-------------------------------------------------------------------------------
Ejercicio 3.16: Un desafío de formato
-------------------------------------------------------------------------------

'''
import csv

def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario'
    camion = []
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            diccionario = {'nombre':row[0], 'cajones':int(row[1]), 'precio': float(row[2])}
            camion.append(diccionario)
    return camion

def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        for row in rows:
            try:  
                fruta = row[0]
                precio = float(row[1])
                diccionarioFrutas[fruta] = precio
            except:
                pass
    return diccionarioFrutas

def hacer_informe(camion, precios):
    listaInforme= []
    cambio=0
    for i in camion:
        for item in precios.items():
            if item[0]==i['nombre']:
                cambio= item[1]-i['precio']
            tabla=(i['nombre'],i['cajones'],i['precio'],round(cambio,2))
        listaInforme.append(tabla)
    return listaInforme

def encabezado():
    headers = ('Nombre', 'Cajones', 'Precio','Cambio')
    espacio=''
    tupla="{:3}{:10}{}{:10}{:2}{:10}{}{:10}".format(espacio,headers[0],espacio,headers[1],espacio,headers[2],espacio,headers[3])
    tupla2='\n{:1}{:>10s}{:1}{:10}{:1}{:10}{:1}{:10}'.format(espacio,'----------',espacio,'----------',espacio,'----------',espacio,'----------')
    return tupla+tupla2

precios = leer_precios('../Data/precios.csv')
camion=leer_camion("Data/camion.csv")

informe = hacer_informe(camion, precios)
print("--------------------------------------------")
print("{:^40}".format("INFORME"))
print("--------------------------------------------")
tabla=encabezado()
print(tabla)
for nombre, cajones, precio, cambio in informe:
    p='$'+str(precio)
    print(f'{nombre:>10s}{cajones:>10d}{p:>10}{cambio:>10.2f}')
print("--------------------------------------------")
