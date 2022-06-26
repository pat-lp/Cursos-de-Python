'''
------------------------------------------------------------------------------
Secuencia binaria
------------------------------------------------------------------------------
Para nosotres, una secuencia binaria es una lista que contiene solo 0’s y 1’s. Por ejemplo s = [0, 1, 0, 0, 1] es una secuencia binaria de longitud 5. La primera secuencia binaria de esa longitud es [0, 0, 0, 0, 0], mientras que la última es [1, 1, 1, 1, 1]. Cada secuencia tiene una siguiente (salvo la última). No vamos a dar una definición precisa, pero escencialmente las secuencias pueden pensarse como representando números enteros en base dos y la siguiente secuencia es la que representa al siguiente número.
------------------------------------------------------------------------------
'''

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


#De cero a uno
print(incrementar([0,0,0,0,0]))#[0, 0, 0, 0, 1]

#De seis a siete
print(incrementar([0,0,1,1,0]))#[0, 0, 1, 1, 1]

#De siete a ocho
print(incrementar([0,0,1,1,1]))#[0, 1, 0, 0, 0]

#De treinta y uno a treinta y dos
print(incrementar([1,1,1,1,1]))#[0, 0, 0, 0, 0]