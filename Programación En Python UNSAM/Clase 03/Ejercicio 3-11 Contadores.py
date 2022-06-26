'''
-------------------------------------------------------------------------------
Ejercicio 3.11: Contadores
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''

import csv
from collections import Counter

def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario'
    camion = []
    f=open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        diccionario = {'nombre':row[0], 'cajones':int(row[1]), 'precio': float(row[2])}
        camion.append(diccionario)
    f.close()
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
    f.close()
    return diccionarioFrutas

precios = leer_precios('../Data/precios.csv')
print(precios)
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

#%% Uso de Counter()

print("---------------------------------------")
print("Uso de Counter()")
print("---------------------------------------")

camion = leer_camion('../Data/camion.csv')
tenencias = Counter()

for s in camion:
      tenencias[s['nombre']] += s['cajones']

print(tenencias)
#%% Recuperar valores individuales

print(tenencias['Mandarina'])
print(tenencias['Naranja'])

#%%

print("Las tres frutas con más cajones\n", tenencias.most_common(3))
print("La fruta con más cajones\n", tenencias.most_common(1))

#%% Imprimo un contador para otro camión

camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()

for s in camion2:
          tenencias2[s['nombre']] += s['cajones']

print(tenencias)
#%% Combina los dos camiones
print("---------------------------------------------------------------------")
print("Camión Uno= ",tenencias,"\n")
print("Camión Dos= ",tenencias2)

combinada = tenencias + tenencias2
print("---------------------------------------------------------------------")
print("Combina ambos camiones\n",combinada)