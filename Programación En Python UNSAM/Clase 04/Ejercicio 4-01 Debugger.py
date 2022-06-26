'''
-------------------------------------------------------------------------------
Ejercicio 4.01: Debugger
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
'''

def invertir_lista(lista):
    '''Recibe una lista L y la devuelve invertida'''
    invertida =[]
    i= len(lista)
    while i > 0: #tomo el último elemento
        i = i -1
        invertida.append (lista.pop(i)) # Con 'pop' estoy eliminando los valores de la lista
    return invertida

lista = [1,2,3,4,5]
listaInvertida= invertir_lista(lista)
print(f'Entrada{lista}, Salida: {listaInvertida}')

#SALIDA: Entrada[], Salida: [5, 4, 3, 2, 1]
#Entrada[] queda vacía ya que la función eliminó todos los valores de la lista