'''
-------------------------------------------------------------------------------
Ejercicio 5.08: Guardar Temperaturas
-------------------------------------------------------------------------------
Ampliá el código de la función medir_temp(n) en tu archivo termometro.py que 
escribiste en el Ejercicio 5.6 para que además de devolver las temperaturas 
simuladas, guarde el vector con estas temperaturas en el directorio Data de tu 
carpeta de ejercicios, en un archivo llamado temperaturas.npy. Hacé que corra 
n = 999 veces.
-------------------------------------------------------------------------------
'''

import random
import statistics
import numpy as np

def medir_temp(n):
    mu=0 #media
    sigma=0.2 #desvío estándar
    temperaturaReal= 37.5 #grados
    mediciones=[(abs(random.normalvariate(mu,sigma)-temperaturaReal)) for i in range(n)]
    return mediciones


def resumen_temp(n):
    mediciones=medir_temp(n)
    return (round(max(mediciones),1), round(min(mediciones),1), round(statistics.mean(mediciones),1), round(statistics.median(mediciones),1))

n=999
medicionesTemperatura=medir_temp(n)
print("Lista de registros de temperatura\n",medicionesTemperatura)
print()
resumenTemperaturas=resumen_temp(n)
print("MÁXIMO,MÍNIMO,PROMEDIO,MEDIANA\n",resumenTemperaturas)

array=np.array(medicionesTemperatura)

np.save('../Data/temperaturas',array) #guardar

cargarArray=np.load('../Data/temperaturas.npy') #cargar
print("CARGAR ARRAY\n",cargarArray)

