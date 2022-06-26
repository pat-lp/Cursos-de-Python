'''
-------------------------------------------------------------------------------
Random walk
-------------------------------------------------------------------------------
'''

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000

plt.plot(randomwalk(N))
plt.show()