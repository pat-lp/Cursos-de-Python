# -*- coding: utf-8 -*-
'''
-------------------------------------------------------------------------------
Ejercicio 5.06: Gaussiana
-------------------------------------------------------------------------------
on random.random() generamos valores aleatorios entre 0 y 1 con una distribución 
uniforme. En esa distribución, todos los valores posibles tienen la misma 
probabilidad de ser seleccionados. También es posible generar valores aleatorios 
con otras distribuciones. Una de las distribuciones más importantes es la 
distribución normal o Gaussiana.

Error absoluto: diferencia entre el valor medido y el valor real.
-------------------------------------------------------------------------------
'''

import random
import statistics

def medir_temp(n):
    mu=0 #media
    sigma=0.2 #desvío estándar
    temperaturaReal= 37.5 #grados
    mediciones=[(abs(random.normalvariate(mu,sigma)-temperaturaReal)) for i in range(n)]
    return mediciones


def resumen_temp(n):
    mediciones=medir_temp(n)
    return (round(max(mediciones),1), round(min(mediciones),1), round(statistics.mean(mediciones),1), round(statistics.median(mediciones),1))

n=99
print("Lista de registros de temperatura\n",medir_temp(n))
print()
resumenTemperaturas=resumen_temp(n)
print("MÁXIMO,MÍNIMO,PROMEDIO,MEDIANA\n",resumenTemperaturas)

print("-----------------------------")
print("{:^30}".format("RESULTADOS"))
print("-----------------------------")
print("MÁXIMO:   ", resumenTemperaturas[0])
print("MÍNIMO:   ", resumenTemperaturas[1])
print("PROMEDIO: ", resumenTemperaturas[2])
print("MEDIANA:  ", resumenTemperaturas[3])
print("------------------------------")
