'''
-------------------------------------------------------------------------------
Ejercicio 1.9: Calculadora de adelantos
-------------------------------------------------------------------------------
¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando 
en el sexto año de la hipoteca (es decir, luego de 5 años)?

Modificá tu programa de forma que la información sobre pagos extras sea 
incorporada de manera versátil. Agregá las siguientes variables antes del 
ciclo, para definir el comienzo, fin y monto de los pagos extras:

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
Hacé que el programa tenga en cuenta estas variables para calcular el total a 
pagar apropiadamente.
-------------------------------------------------------------------------------
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes+=1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo *(1+tasa/12)-(pago_mensual + pago_extra)
        total_pagado += (pago_mensual + pago_extra)
    else:
        saldo = saldo *(1+tasa/12)-pago_mensual
        total_pagado += pago_mensual
    print("Saldo {} - Mes: {}".format(round(saldo,4),mes))

print("-----------------------------")
print("Total pagado: ",round(total_pagado,2))
print("-----------------------------")