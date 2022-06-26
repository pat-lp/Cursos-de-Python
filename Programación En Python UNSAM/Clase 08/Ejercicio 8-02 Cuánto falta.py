'''
-------------------------------------------------------------------------------
Ejercicio 8.2: Cuánto falta
-------------------------------------------------------------------------------
Un conocido canal Argentino tiene por costumbre anunciar la cantidad de días 
que faltan para la próxima primavera.
Escribí un programa que asista a los técnicos del canal indicándoles, al correr 
el programa el número que deben poner en la placa.
-------------------------------------------------------------------------------
'''

from datetime import datetime, date

def proxima_primavera():
    '''
    Calcula la cantidad de días hasta la primavera
    Pre: Tiene en cuenta la fecha actual.
    Pos: Devuelve la cantidad de días en un número entero.
    '''
    hoy = date.today()
    #Si el mes es mayor a 9 se le suma 1 a hoy.year para que considere el próximo año.
    if hoy.month >= 9:
        primavera = date(year = hoy.year+1, month = 9, day = 21)
        hoy = date(year = hoy.year, month= hoy.month, day= hoy.day)
        dias= primavera - hoy
    else:
        primavera = date(year = hoy.year, month = 9, day = 21)
        hoy = date(year = hoy.year, month= hoy.month, day= hoy.day)
        dias= primavera - hoy
    
    return dias.days

print("******************************************")
print(f"Mientras tanto....\nFALTAN {proxima_primavera()} DIAS PARA LA PRIMAVERA")
print("******************************************")