

import informe_final

print('FORMATO html')
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt='html')
print()

print('FORMATO txt')
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt = 'txt')
print()

print('FORMATO csv')
informe_final.informe_camion('../Data/camion.csv', '../Data/precios.csv', fmt = 'csv')