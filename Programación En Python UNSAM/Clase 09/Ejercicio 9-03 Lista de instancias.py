'''
-------------------------------------------------------------------------------
Ejercicio 9.3: Lista de instancias
-------------------------------------------------------------------------------
Seguí estos pasos para crear una lista de las instancias de Lote (una lista de objetos Lote) a partir de una lista de diccionarios. Luego calculá el precio total de todas esas instancias. Para poder importar fileparse, primero copialo a la carpeta de ejercicios de la clase actual. La última versión que deberías tener es la correspondiente al Ejercicio 7.6.
-------------------------------------------------------------------------------
'''

import fileparse
import lote

with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select= ['nombre', 'cajones', 'precio'], types= [str, int, float])
    
    
camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(camion)

print(sum([c.costo() for c in camion]))#47671.15