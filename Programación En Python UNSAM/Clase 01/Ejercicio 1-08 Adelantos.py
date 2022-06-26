'''
-------------------------------------------------------------------------------
Ejercicio 1.8: Adelantos
-------------------------------------------------------------------------------
Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 
12 meses de la hipoteca. Modificá el programa para incorporar estos pagos 
extra y que imprima el monto total pagado junto con la cantidad de meses 
requeridos.
Cuando lo corras, este nuevo programa debería dar un pago 
total de 929965.62 en 342 meses.

Aclaración: aunque puede parecer sencillo, este ejercicio requiere que 
agregues una variable mes y que prestes bastante atención a cuándo la 
incrementás, con qué valor entra al ciclo y con qué valor sale del ciclo. 
Una posiblidad es inicializar mes en 0 y otra es inicializarla en 1. 
En el primer caso es problable que la variable salga del ciclo contando 
la cantidad de pagos que se hicieron, en el segundo, 
¡es probable que salga contando la cantidad de pagos más uno!
-------------------------------------------------------------------------------
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0

while saldo > 0:
    mes+=1
    print("Saldo {} - Mes: {}".format(round(saldo,4),mes))
    if mes <= 12:
        saldo = saldo *(1+tasa/12)-(pago_mensual+1000)
        total_pagado += (pago_mensual+1000)
    else:
        saldo = saldo *(1+tasa/12)-pago_mensual
        total_pagado += pago_mensual

print("-----------------------------")
print("Total pagado: ",round(total_pagado,2))
print("-----------------------------")