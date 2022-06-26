'''
------------------------------------------------------------------------------
Ejercicio 2.9: Funciones de la biblioteca
------------------------------------------------------------------------------
El módulo csv se puede usar cada vez que tengas que  hay que leer archivos CSV. 

Tu programa debería imprimir una salida como la siguiente:
Costo total 47671.15
------------------------------------------------------------------------------
'''
import csv

def costo_camion(nombre_archivo):
    costoTotal=0
    f=open(nombre_archivo)
    rows=csv.reader(f)
    next(rows)
    for row in rows:
        try:
            costoTotal+=int(row[1])*float(row[2])
        except ValueError:
            print("Error")
    f.close()
    return costoTotal


costoTotal=costo_camion('../Data/camion.csv')

print("------------------------------------------------------------")
print("El costo total por los cajones cargados es de: ",costoTotal) #47671.15
print("------------------------------------------------------------")


