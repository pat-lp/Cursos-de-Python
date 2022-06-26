'''
------------------------------------------------------------------------------
Ejercicio 2.4: Archivos comprimidos gzip
------------------------------------------------------------------------------
La función primitiva de Python open() no lee archivos comprimido en gzip. Pero
hay un módulo de la biblioteca de Python llamado gzip que lee archivos comprimidos.

>>> import gzip
>>> with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')
... mirá la salida ...

Observación: La inclusión del modo 'rt' es crítica acá. Si te lo olvidás, vas 
a estar leyendo cadenas de bytes en lugar de cadenas de caracteres.
------------------------------------------------------------------------------
'''

import gzip

print("Archivos gzip\n")

with gzip.open('../Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')