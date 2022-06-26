'''
------------------------------------------------------------------------------
Ejercicio 2.6: Transformar un script en una función
------------------------------------------------------------------------------
Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de 
la sección anterior) en una función costo_camion(nombre_archivo). Esta función
recibe un nombre de archivo como entrada, lee la información sobre los 
cajones que cargó el camión y devuelve el costo de la carga de frutas como 
una variable de punto flotante.
------------------------------------------------------------------------------
'''
#Para usar tu función, cambiá el programa de forma que se parezca a esto:

def costo_camion(nombre_archivo):
    costoTotal=0
    f=open(nombre_archivo)
    next(f)
    for line in f:
        row = line.split(",")
        costoTotal+=int(row[1])*float(row[2])
    f.close()
    return costoTotal


costo = costo_camion('../Data/camion.csv')
print("\n-----------------------------")
print('Costo total:', costo) #47671.15
print("-----------------------------")


