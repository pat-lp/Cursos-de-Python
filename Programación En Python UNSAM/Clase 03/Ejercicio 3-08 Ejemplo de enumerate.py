'''
-------------------------------------------------------------------------------
Ejercicio 3.08: Ejemplo práctico de enumerate()
-------------------------------------------------------------------------------
Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de un
camión, pero tiene algunas filas que faltan. Usando enumerate(), modificá tu 
programa costo_camion.py de forma que imprima un aviso (warning) cada vez que 
encuentre una fila incorrecta.

>>> cost = costo_camion('../Data/missing.csv')
Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
Fila 7: No pude interpretar: ['Naranja', '', '70.44']
>>>
Para hacer esto, vas a tener que cambiar algunas partes de tu código.

...
for n_fila, fila in enumerate(filas, start=1):
    try:
        ...
    except ValueError:
        print(f'Fila {n_fila}: No pude interpretar: {fila}')

-------------------------------------------------------------------------------
'''

