'''
------------------------------------------------------------------------------
Ejercicio 1.11: Bonus
------------------------------------------------------------------------------
Ya que estamos, corregí el código anterior de forma que el pago del último mes 
se ajuste a lo adeudado.
------------------------------------------------------------------------------
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
    if (pago_extra_mes_comienzo <= mes) and (mes <= pago_extra_mes_fin):
        a_pagar = pago_mensual+pago_extra
    else:
        a_pagar = pago_mensual
    if saldo *(1+tasa/12) < a_pagar:
        a_pagar=saldo *(1+tasa/12)
    saldo = saldo *(1+tasa/12) - a_pagar
    total_pagado += a_pagar
    print("Mes: {}   Total pagado: {}   Saldo: {} ".format(mes,round(total_pagado,2) ,round(saldo,2)))

print("-----------------------------")
print("Total pagado: ",round(total_pagado,2))
print("-----------------------------")