'''
-------------------------------------------------------------------------------
Ejercicio "termometro"
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

#Función para probar lo realizado
def main():
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
    return "Fin función main()"

#print(main())

