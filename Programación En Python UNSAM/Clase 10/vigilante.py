'''
------------------------------------------------------------------------------
Ejercicio 10.7: Cambios de precio de un camión
------------------------------------------------------------------------------
Modificá el código del Ejercicio 10.5 de modo que la lectura del archivo esté 
resuelta por una única función generadora vigilar() a la que se le pasa un 
nombre de archivo como parámetro. 
------------------------------------------------------------------------------
'''

import os
import time

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


if __name__ == '__main__':
    import informe_final
    camion = informe_final.leer_camion('../Data/camion.csv')
    
    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
            