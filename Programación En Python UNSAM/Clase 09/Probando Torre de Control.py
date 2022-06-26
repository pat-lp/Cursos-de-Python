'''
-------------------------------------------------------------------------------
Probando Torre de Control
-------------------------------------------------------------------------------
'''

import torre_control


torre = torre_control.TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nueva_partida('SS10')
torre.nuevo_arribo('AR32')
torre.ver_estado()
#Vuelos esperando para aterrizar: AR156, AR32
#Vuelos esperando para despegar: KLM1267
torre.asignar_pista()#El vuelo AR156 aterrizó con éxito.
torre.asignar_pista()#El vuelo AR32 aterrizó con éxito.
torre.asignar_pista()#El vuelo KLM1267 despegó con éxito.
torre.asignar_pista()#No hay vuelos en espera.