'''
------------------------------------------------------------------------------
Ejercicio 10.5: Monitoreo de datos en tiempo real.
------------------------------------------------------------------------------
Este generador que busca un archivo y entrega las líneas que incluyen 
cierto substring.
------------------------------------------------------------------------------
'''

import os
import time

f = open('../Data/mercadolog.csv')
f.seek(0, os.SEEK_END) 

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.5)
        continue
    fields = line.split(',')
    nombre = fields[0].strip('"')
    precio = float(fields[1])
    volumen = int(fields[2])
    if volumen > 1000:
        print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')