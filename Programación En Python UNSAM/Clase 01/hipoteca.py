'''
------------------------------------------------------------------------------
Ejercicio 1.11: Bonus
------------------------------------------------------------------------------
Ya que estamos, corregí el código anterior de forma que el pago del último mes 
se ajuste a lo adeudado.
------------------------------------------------------------------------------
'''
# Datos:
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
ultimo_saldo=0


while saldo > 0:
    mes+=1
    # Pago extra a partir del sexto año por cuatro años
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo *(1+tasa/12)-(pago_mensual + pago_extra)
        total_pagado += (pago_mensual + pago_extra)
    else:
        saldo = saldo *(1+tasa/12)-pago_mensual
        total_pagado += pago_mensual

    # Modificación del último pago por saldo negativo
    if saldo < 0:
        ultimo_saldo= saldo 
        saldo = 0
        total_pagado += ultimo_saldo
    print("Mes: {}   Total pagado: {}   Saldo: {} ".format(mes,round(total_pagado,2) ,round(saldo,2)))

print("-----------------------------")
print("Total pagado: ",round(total_pagado,2))
print("-----------------------------")