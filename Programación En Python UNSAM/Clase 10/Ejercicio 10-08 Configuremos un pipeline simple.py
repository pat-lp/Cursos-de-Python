'''
------------------------------------------------------------------------------
Ejercicio 10.8: Configuremos un pipeline simple
------------------------------------------------------------------------------
'''
import time
import os


def vigilar(filename):
    '''
    Función generadora a la que se le pasa un nombre 
    de archivo por parámetro.
    '''
    f= open(filename)
    f.seek(0, os.SEEK_END) 
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)
            continue
        yield line

def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
            
            
lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
    print(line)