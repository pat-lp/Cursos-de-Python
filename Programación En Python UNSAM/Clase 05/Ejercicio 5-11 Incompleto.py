'''
-------------------------------------------------------------------------------
Ejercicio 5.11: Incompleto
-------------------------------------------------------------------------------
Cuál sería el comando de Python que nos dice si hay al menos un cero en el 
vector que representa el álbum? ¿Qué significa que haya al menos un cero en 
nuestro vector?

Implementá la función album_incompleto(A) que recibe un vector y devuelve 
True si el álbum A no está completo y False si está completo.
------------------------------------------------------------------------------
'''
import numpy as np


def album_incompleto(A):
    #Devuelve True si no está completo y False si está completo
    return np.any(A==0)



#Es interesante que five_up da un arreglo de valores booleanos. True si satisface la condición y False si no la satisface.
A=np.array([1,1,2,0,4])
print(album_incompleto(A))