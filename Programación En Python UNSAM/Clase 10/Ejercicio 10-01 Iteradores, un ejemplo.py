'''
------------------------------------------------------------------------------
Ejercicio 10.1: Iteradores, un ejemplo
------------------------------------------------------------------------------
Construí la siguiente lista:

a = [1, 9, 4, 25, 16]
Y ahora iterá sobre esa lista a mano: Llamá al método __iter__() para obtener 
un objeto iterador y llama al método __next__() para obtener sucesivamente cada 
uno de los elementos.
------------------------------------------------------------------------------
'''

a = [1, 9, 4, 25, 16]

i = a.__iter__()
#print(i)#<list_iterator object at 0x000000BBB1F61850>

print(i.__next__())#1

print(i.__next__())#9

print(i.__next__())#4

print(i.__next__())#25

print(i.__next__())#16

#print(i.__next__())#StopIteration

#%% CON UN ARCHIVO

f = open('../Data/camion.csv')
f.__iter__()    # Notar que esto apunta al método...
                    # ...que accede al archivo mismo.
print(next(f))#'nombre,cajones,precio\n'
print(next(f))#'Lima,100,32.20\n'
print(next(f))#'Naranja,50,91.10\n'

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
#print(next(f))#StopIteration
