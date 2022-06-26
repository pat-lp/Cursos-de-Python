'''
-------------------------------------------------------------------------------
Ejercicio 6.12: Un poco más allá
-------------------------------------------------------------------------------
Modificá el archivo costo_camion.py para que use la función informe_funciones.leer_camion() del programa informe_funciones.py.
-------------------------------------------------------------------------------
'''

from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    costoTotal=0
    for i in leer_camion(nombre_archivo):
         try:
            costoTotal+=int(i['cajones'])*float(i['precio'])
         except ValueError:
            print("Error")
    return costoTotal

costoTotal=costo_camion('../Data/camion.csv')

print("------------------------------------------------------------")
print("El costo total por los cajones cargados es de: ",costoTotal) #47671.15
print("------------------------------------------------------------")
