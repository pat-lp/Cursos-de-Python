'''
-------------------------------------------------------------------------------
Ejercicio 9.13: implementar el TAD pila
-------------------------------------------------------------------------------
'''

class Pila:
    '''Representa a una Pila, con operaciones de apilar y desapilar.
    El último en ser apilado es el primero en ser desapilado.
    '''
    def __init__(self):
        '''Crea una Pila vacia.'''
        self.items = []

    def apilar(self, x):
        '''Apila el elemento x.'''
        self.items.append(x)

    def desapilar(self):
        '''Elimina el último elemento de la Pila 
        y devuelve su valor. 
        Si la Pila esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La Pila esta vacia')
        return self.items.pop()

    def esta_vacia(self):
        '''Devuelve 
        True si la Pila esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
#%%

def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")
    
pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)