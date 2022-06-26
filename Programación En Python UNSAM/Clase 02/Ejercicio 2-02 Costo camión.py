'''
------------------------------------------------------------------------------
Ejercicio 2.2: Costo camión
------------------------------------------------------------------------------
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de 
cajones cargados en el camión, y un precio de compra por cada cajón de ese 
grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
lea las líneas, y calcule el precio pagado por los cajones cargados 
en el camión.
Ayuda: para interpretar un string s como un número entero, usá int(s). Para 
leerlo como punto flotante, usá float(s).

Tu programa debería imprimir una salida como la siguiente:
Costo total 47671.15
------------------------------------------------------------------------------
'''
costoTotal=0
f = open('C:/Users/Patricia/Desktop/Programacion_en_Python_UNSAM/ejercicios_python/Clase02/Data/camion.csv', 'rt')
headers =next(f).split(",")

for line in f:
    row = line.split(",")
    costoTotal+=int(row[1])*float(row[2])
print("------------------------------------------------------------")
print("El costo total por los cajones cargados es de: ",costoTotal)
print("------------------------------------------------------------")
f.close()