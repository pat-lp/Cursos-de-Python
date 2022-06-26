'''
------------------------------------------------------------------------------
Ejercicio 6-03: Propagar con cadenas
------------------------------------------------------------------------------
'''

def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#%% CÓDIGO MODIFICADO

print("--------------------------------------------------------------")
print("Código modificado")
print("--------------------------------------------------------------")

def trad2s_(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l_(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s_(l)
    if debug:
        print(s)#, end = ' -> ')
    W=s.split('x') #corta la cadena hasta -1
    PW=[w if ('f' not in w) else 'f'*len(w) for w in W]
    ps='x'.join(PW) #SE AGREGA:'x' para que tome en cuenta el -1 que se saco antes.
    if debug:
        print(ps)
    return trad2l_(ps)

l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)


#%% PREGUNTAS:
'''
1-¿Porqué se acorta la lista?
Rta:
    Porque no toma en cuenta el -1, directamente lo saca del vector.
    
2-¿Podés corregir el error agregando un solo caracter al código?

3-¿Te parece que este algoritmo es cuadrático como el Ejercicio 6.1 o lineal 
como el Ejercicio 6.2?
Rta:
    Es un algoritmo lineal.
'''