'''
-------------------------------------------------------------------------------
Ejercicio 5.10: Crear
-------------------------------------------------------------------------------
Implementá la función crear_album(figus_total) que devuelve un álbum (vector) 
vacío con figus_total espacios para pegar figuritas.
------------------------------------------------------------------------------
'''
import numpy as np
#verctor vacio

def crear_album(figus_total):
    #Devuelve vector vacio
    return np.zeros(figus_total,dtype=int)

n=670

print(f"Creo un albúm con {n} figuritas:\n {crear_album(n)}")