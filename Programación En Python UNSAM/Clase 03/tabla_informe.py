'''
-------------------------------------------------------------------------------
Ejercicio 3.15: Agregar encabezados
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''
import csv


def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario'
    camion = []
    f=open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        diccionario = {'nombre':row[0], 'cajones':int(row[1]), 'precio': float(row[2])}
        camion.append(diccionario)
    return camion


def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    f = open(nombre_archivo)
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

total=0.0
venta=0.0

for s in camion:
    total+=s['cajones']*s['precio']
    if precios[s['nombre']] !=0:
        venta+=precios[s['nombre']]*s['cajones']


print("---------------------------------------")
print("Costo del camión: {}\nVenta en el negocio: {}\nBalance: {}".format(total,venta,round(venta-total,2)))
print("---------------------------------------")
print()

#%% Informe con encabezado

print()
informe = hacer_informe(camion, precios)
print("--------------------------------------------")
print("{:^40}".format("INFORME"))
print("--------------------------------------------")
tabla=encabezado()
print(tabla)
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s}{cajones:>10d}{precio:10.2f}{cambio:10.2f}')
    
print("--------------------------------------------")






