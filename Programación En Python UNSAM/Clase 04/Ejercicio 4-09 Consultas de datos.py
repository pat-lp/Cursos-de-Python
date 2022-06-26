'''
-------------------------------------------------------------------------------
Ejercicio 4.09: Consultas de datos
-------------------------------------------------------------------------------
Calculá el costo total de la carga del camión en un solo comando.
-------------------------------------------------------------------------------
'''
#Primero, generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.
import csv
import pprint

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


camion = leer_camion('../Data/camion.csv')

mas100 = [ s for s in camion if s['cajones']>100]

print("\nTodas las frutas con más de 100 cajones en el camión")
pprint.pprint(mas100)

#Ahora, una con la info sobre cajones de Mandarina y Naranja.

myn = [ s for s in camion  if s['nombre'] in {'Mandarina','Naranja'}]
print("\nInformación sobre cajones de Mandarina y Naranja")
pprint.pprint(myn)



#O una con la info de las frutas que costaron más de $10000.
costo10k = [s for s in camion   if s['cajones']*s['precio']> 10000]

print("\nFrutas que costaron más de $10000")
pprint.pprint(costo10k)