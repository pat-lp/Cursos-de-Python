'''
-------------------------------------------------------------------------------
Ejercicio 8.3: Fecha de reincorporación
-------------------------------------------------------------------------------
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 y 
dura 200 días, ¿qué día te reincorporás al trabajo?
-------------------------------------------------------------------------------
'''

#from datetime import timedelta
from datetime import datetime, timedelta

def licencia_por_maternidad(fecha_comienzo):
    fin_licencia = fecha_comienzo + timedelta(days = 200)
    return fin_licencia.strftime('%d/%m/%Y')

fecha_comienzo = datetime(2020,9,26)
print(f"Licencia por maternidad comienza el día {fecha_comienzo.strftime('%d/%m/%Y')} y finaliza después de 200 días la fecha {licencia_por_maternidad(fecha_comienzo)}")

