'''
-------------------------------------------------------------------------------
Ejercicio 3.09: La función zip()
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''
import csv

def costo_camion(nombre_archivo):
    costo_total=0
    f= open(nombre_archivo)
    filas=csv.reader(f)
    encabezados = next(filas)
    
    for n_fila,fila in enumerate (filas, start=1):
        record= dict(zip(encabezados,fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa los errores en los int() y float() de arriba
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    f.close()
    return costo_total

camion=costo_camion("../Data/fecha_camion.csv")
print("-----------------------------------------------")
print("Costo camión: ",camion)
print("-----------------------------------------------")

#%% Se modifica  el ejericio 2.18


def leer_camion(nombre_archivo):
    'Devuelve una lista con un diccionario, se agrega dict(zip())'
    camion = []
    f=open(nombre_archivo)
    filas = csv.reader(f)
    encabezados= next(filas)
    for n_fila,fila in enumerate(filas):
        record = dict(zip(encabezados,fila))
        try:
            lote={'nombre':record['nombre'],'cajones':int(record['cajones']),'precio':float(record['precio'])}
            camion.append(lote)
        except ValueError:
            print(f"Error en fila {n_fila}")
    f.close()
    return camion


def leer_precios(nombre_archivo):
    'Devuelve un diccionario con las frutas y sus precios'
    diccionarioFrutas ={}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for row in rows:
        try:  
            diccionarioFrutas[row[0]] = float(row[1])
        except IndexError:
            print("Error en una línea")
    f.close()
    return diccionarioFrutas

precios = leer_precios('../Data/precios.csv')
camion=leer_camion("../Data/fecha_camion.csv")

total=0.0
venta=0.0

for s in camion:
    total+=s['cajones']*s['precio']
    if precios[s['nombre']] !=0:
        venta+=precios[s['nombre']]*s['cajones']


print("---------------------------------------")
print("Costo del camión: {}\nVenta en el negocio: {}\nBalance: {}".format(total,venta,round(venta-total,2)))
print("---------------------------------------")
