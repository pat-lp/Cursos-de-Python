'''
------------------------------------------------------------------------------
Ejercicio 10.12: El pipeline ensamblado
------------------------------------------------------------------------------
'''

from ticker import ticker

ticker('../Data/camion.csv','../Data/mercadolog.csv','txt')

ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'csv')