'''
-------------------------------------------------------------------------------
Ejercicio 9.10: Ejemplo de getattr()
-------------------------------------------------------------------------------
'''

import lote
c= lote.Lote('Peras', 100, 490.1)
columnas = ['nombre','cajones']

for colname in columnas:
    print(colname, '=', getattr(c, colname))
    

#%%

import informe_final
from formato_tabla import crear_formateador, imprimir_tabla

camion = informe_final.leer_camion('../Data/camion.csv')

formateador = crear_formateador('txt')

imprimir_tabla(camion, ['nombre','cajones'], formateador)

imprimir_tabla(camion, ['nombre','cajones','precio'], formateador)