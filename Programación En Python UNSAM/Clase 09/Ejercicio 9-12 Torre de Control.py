'''
-------------------------------------------------------------------------------
Ejercicio 9.12: Torre de Control
-------------------------------------------------------------------------------
Usando un par de objetos de la clase Cola, escribí una nueva clase llamada 
TorreDeControl que modele el trabajo de una torre de control de un aeropuerto 
con una pista de aterrizaje. Los aviones que están esperando para aterrizar 
tienen prioridad sobre los que están esperando para despegar. 
-------------------------------------------------------------------------------
'''

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0



class TorreDeControl:
    '''
    Modela el trabajo de una torre de control de un aeropuerto con una pista de aterrizaje.
    '''
    def __init__(self):
        self.arribo = Cola()
        self.partida = Cola()

    def nuevo_arribo(self, vuelo_ingresa):
        '''
        Aviones que están esperando para aterrizar.
        '''
        self.arribo.encolar(vuelo_ingresa)

    def nueva_partida(self, vuelo_sale):
        '''
        Aviones que estan esperando para despegar.
        '''
        self.partida.encolar(vuelo_sale)

    def asignar_pista(self):
        '''
        Se asignan pistas a los vuelos según aterrizan ó despegan.
        En caso de que no hubieran vuelos para asignar una pista se imprime por pantalla.
        '''
        if not self.arribo.esta_vacia():
            print("El vuelo " + self.arribo.desencolar() + " aterrizó con éxito.")
        elif not self.partida.esta_vacia():
            print("El vuelo " + self.partida.desencolar() + " despegó con éxito.")
        else:
            print("No hay vuelos en espera.")

    def ver_estado(self):
        '''
        Imprime los vuelos que estan esperando para aterrizar o despegar.
        '''
        if not self.arribo.esta_vacia():
            print("Vuelos esperando para aterrizar: " + ", ".join(self.arribo.items))
        
        if not self.partida.esta_vacia():
            print("Vuelos esperando para despegar: " + ", ".join(self.partida.items))
 
