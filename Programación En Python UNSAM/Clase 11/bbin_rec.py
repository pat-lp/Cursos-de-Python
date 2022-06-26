'''
-------------------------------------------------------------------------------
Ejercicio 11.11: Búsqueda binaria
-------------------------------------------------------------------------------
Escribí una función recursiva bbinaria_rec(lista, e) que implemente la búsqueda 
binaria de un elemento e en una lista ordenada lista. La función debe devolver 
simplemente True o False indicando si el elemento está o no en la lista. 

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        # completar
    return res
-------------------------------------------------------------------------------
'''

def bbinaria_rec(lista, e):
    '''
    Búsqueda de un elemento en una lista.
    Pre: La lista tiene que estar ordenada.
    Pos: Devuelve True or False si encuentra el elemento dado. 
    '''
    res= True
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            return res 
        if e > lista[medio]:
            return bbinaria_rec(lista[medio+1:], e)
        else:
            return bbinaria_rec(lista[:medio], e)
    return res



def f_principal():
    lista = [1, 2, 4, 8, 12, 22]
    
    e0 = 1
    print(f'El valor {e0} esta en la lista {lista}: {bbinaria_rec(lista, e0)}')#True
    
    e1 = 2
    print(f'El valor {e1} esta en la lista {lista}: {bbinaria_rec(lista, e1)}')#True
    
    e2 = 4
    print(f'El valor {e2} esta en la lista {lista}: {bbinaria_rec(lista, e2)}')#True
    
    e3 = 3
    print(f'El valor {e3} esta en la lista {lista}: {bbinaria_rec(lista, e3)}')#False
    
    e4 = 7
    print(f'El valor {e4} esta en la lista {lista}: {bbinaria_rec(lista, e4)}')#False
    
    e5 = 12
    print(f'El valor {e5} esta en la lista {lista}: {bbinaria_rec(lista, e5)}')#True
    
    e6 = 22
    print(f'El valor {e6} esta en la lista {lista}: {bbinaria_rec(lista, e6)}')#True
    
    e7 = 23
    print(f'El valor {e7} esta en la lista {lista}: {bbinaria_rec(lista, e7)}')#False
    
        
    
if __name__ == '__main__':
    f_principal()
