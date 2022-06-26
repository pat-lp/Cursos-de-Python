'''
-------------------------------------------------------------------------------
Ejercicio 7.11: Subplots fuera de una grilla
-------------------------------------------------------------------------------
Modificá el siguiente código para reproducir el gráfico que se muestra. Prestá 
atención a cómo se numeran los subplots.
-------------------------------------------------------------------------------
'''

import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

#%%
'''
#SUBPLOT(FILA, COLUMNA, NRO_FIGURA)
Son dos filas de figuras en total, la figura de arriba abarca las tres figuras de 
abajo pero en una sola columna, por lo cual seria (2,1,1), (2,1,2) y  (2,1,3)
Las 3 figuras de la segunda fila se tienen que dividir en 3 columnas, por eso,
(2,3,x) la numeración comenzaría a partir de 4, siendo (2,3,4)-lateral primera
abajo, (2,3,5)-central y (2,3,6)-tercera de abajo.
'''

fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba, son dos filas de figuras en total
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) 
plt.plot([1,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

