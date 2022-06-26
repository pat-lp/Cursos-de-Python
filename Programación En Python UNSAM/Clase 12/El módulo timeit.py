'''
------------------------------------------------------------------------------
El módulo timeit
------------------------------------------------------------------------------
'''

import time
import timeit as tt

print(tt.timeit('time.sleep(1)',number = 1))#Out[3]: 1.0010360410087742

print(tt.timeit('"-".join(str(n) for n in range(100))', number = 1))#Out[4]: 6.670000296551734e-05

print(tt.timeit('"-".join(str(n) for n in range(100))', number = 10000))

print(tt.timeit('"-".join(str(n) for n in range(100))', number = 10000))

print(tt.timeit('"-".join([str(n) for n in range(100)])', number = 10000))
print(tt.timeit('"-".join(map(str, range(100)))', number = 10000))

