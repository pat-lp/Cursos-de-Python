'''
------------------------------------------------------------------------------
Ejercicio 12.4: experimento con 3 métodos
------------------------------------------------------------------------------
Hacé una función generar_lista(N) que genere una lista aleatoria de largo N con 
números enteros del 1 al 1000 (puede haber repeticiones).

Modificá el código de las tres funciones para que cuenten cuántas comparaciones 
entre elementos de la lista realiza cada una. Por ejemplo, ord_seleccion realiza 
comparaciones (entre elementos de la lista) sólo cuando llama a 
buscar_max(lista, a, b) y en ese caso realiza b-a comparaciones.

Realizá un experimento que genere una lista de largo N y la ordene con los tres
métodos (burbujeo, inserción y selección).

Para N = 10, realizá k = 100 repeticiones del siguiente experimento. Generar 
una lista de largo N, ordenarlas con los tres métodos y guardar la cantidad de 
operaciones. Al final, debe imprimir el promedio de comparaciones realizado 
por cada método.
------------------------------------------------------------------------------
'''