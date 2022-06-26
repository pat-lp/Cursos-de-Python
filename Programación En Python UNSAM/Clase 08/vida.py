'''
-------------------------------------------------------------------------------
Ejercicio 8.1: Segundos vividos
-------------------------------------------------------------------------------
Escribí una función llamada vida_en_segundos(fecha_nac) a la que le pasás tu 
fecha de nacimiento y te devuelve la cantidad de segundos que viviste (asumiendo 
que naciste a las 00:00hs de tu fecha de nacimiento). La función debe tomar 
como entrada una cadena en formato 'dd/mm/AAAA' (día, mes, año con 2, 2 y 4 
dígitos, separados con barras normales) y devolver un float.
-------------------------------------------------------------------------------
'''

from datetime import datetime

def vida_en_segundos(fecha_nac):
    '''
    Calcula la cantidad de segundos vividos.
    Pre: Recibe la fecha de nacimiento en formato de cadena 'dd/mm/AAAA'.
    Pos: Devuelve la cantidad de segundos en float.
    '''
    cadena_a_fecha = datetime.strptime(fecha_nac,'%d/%m/%Y')
    return (datetime.today() - cadena_a_fecha).total_seconds()


def f_principal():
    fecha_nacimiento = '01/01/2000'
    print(f"La cantidad de segundos vividos desde la fecha {fecha_nacimiento} hasta {datetime.strftime(datetime.today(),'%d/%m/%Y')} es un total de: {vida_en_segundos(fecha_nacimiento)}")
    fecha_nacimiento2 = '29/09/2021'
    print(f"La cantidad de segundos vividos desde la fecha {fecha_nacimiento2} hasta {datetime.strftime(datetime.today(),'%d/%m/%Y')} es un total de: {vida_en_segundos(fecha_nacimiento2)}")


if __name__ == "__main__":
    f_principal()