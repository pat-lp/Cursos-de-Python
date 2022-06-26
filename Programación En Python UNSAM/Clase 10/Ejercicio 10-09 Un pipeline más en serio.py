'''
------------------------------------------------------------------------------
Ejercicio 10.9: Un pipeline más en serio
------------------------------------------------------------------------------
La salida de la función vigilar() fue usada como entrada a la función 
csv.reader() (que habíamos usado para leer un archivo del disco) y el 
resultado es una secuencia de lineas "parseadas", separadas por las comas.
------------------------------------------------------------------------------
'''

from vigilante import vigilar
import csv

lines = vigilar('../Data/mercadolog.csv')
rows = csv.reader(lines)

for row in rows:
    print(row)