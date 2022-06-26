'''
-------------------------------------------------------------------------------
Ejercicio 5.07: arange() y linspace()
-------------------------------------------------------------------------------
Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). Repetí el ejercicio usando linspace(). ¿Qué diferencia hay en el resultado?
-------------------------------------------------------------------------------
'''

import numpy as np

'''Números impares entre 1 y 19, es decir que terminen en 1,3,5,7 y 9.'''

#linspace()
print(np.linspace(1,19,num=10).round(2))

#arange()
print(np.arange(1,20,2))

#¿Qué diferencia hay en el resultado?
#Arange no incluye el limite superior en los resultados, por lo cual se tiene que 
#poner un núméro más que el solicitado.