'''
-------------------------------------------------------------------------------
Ejercicio 9.11: Canguros buenos y canguros malos
-------------------------------------------------------------------------------
Este ejercicio está relacionado con un error muy común en Python. Escribí una 
definición de una clase Canguro que tenga:

Un método __init__ que recibe un nombre para el canguro y una lista (parámetro 
opcional) e inicializa un atributo llamado contenido_marsupio con la lista que 
le pases como parámetro o como lista vacía si no le pasás nada.
Un método llamado meter_en_marsupio que, dado un objeto cualquiera, lo agregue 
a la lista contenido_marsupio.
Un método __str__ que devuelve una representación como cadena del objeto 
Canguro indicando su nombre y los contenidos de su marsupio.
-------------------------------------------------------------------------------
'''

class Canguro:
    
    def __init__(self, nombre, contenido=None):
        '''
        Inicializar los contenidos del marsupio.
        nombre: string
        contenido: contenido inicial del marsupio, lista. Si se crean distintos 
        objetos de la clase Canguro la lista debería 
        reinicializarse de lo contrario todos los objetos utilizarían la misma lista.
        '''
        self.nombre = nombre
        if contenido is None:
            contenido = []
        self.contenido_marsupio = contenido
        
    def meter_en_marsupio(self, contenido):
        ''' Agrega contenido a las lista '''
        self.contenido_marsupio.append(contenido)
    
    def __str__(self):
        '''Imprime en formato cadena al Canguro con el contenido de su marsupio'''
        t = ['Nombre: '+ self.nombre + ' --> contenido de su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + str(obj)
            t.append(s)
        return '\n'.join(t)+'\n'
        
        
def f_principal():
    madre_canguro = Canguro('Madre')
    madre_canguro.meter_en_marsupio('mantita')
    madre_canguro.meter_en_marsupio('polar')
    cangurito = Canguro('Hijo Cangurito')
    
    madre_canguro.meter_en_marsupio(cangurito)#paso el atributo del objeto "cangurito"
    cangurito.meter_en_marsupio('manta de polar')
    
    cangurito_hijo_dos = Canguro('Hijo Cangurito Dos')
    cangurito_hijo_dos.meter_en_marsupio('manta para hijo dos')
    
    madre_canguro.meter_en_marsupio(cangurito_hijo_dos)
    
    print(madre_canguro)
    print(cangurito)
    print(cangurito_hijo_dos)
    
    
if __name__ == "__main__":
    f_principal()
        
#%%


"""Este código continene un 
bug importante y dificil de ver
"""
'''

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido    #--> Se modifica la inicialización de la lista

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)    #--> s=''+str(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito) 

print(madre_canguro)
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
'''