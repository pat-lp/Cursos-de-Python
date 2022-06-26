'''
-------------------------------------------------------------------------------
Ejercicio 5.16: Ejercicios con paquetes
-------------------------------------------------------------------------------
Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum 
es de 670. Tené en cuenta que, como en la vida real, puede haber figuritas 
repetidas en un paquete.
-------------------------------------------------------------------------------
'''
import random
import numpy as np

def crear_paquete(figus_total):
    paquete=np.linspace(random.randint(1,figus_total)-1,random.randint(1,figus_total)-1,num=5,dtype=np.int64)
    return paquete
    

figus_total=670

print("Paquete: ",crear_paquete(figus_total))