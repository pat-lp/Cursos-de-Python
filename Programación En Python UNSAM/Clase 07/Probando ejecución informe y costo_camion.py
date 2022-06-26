
import informe_final
import costo_camion


print("Utilizando informe.main\n")
informe_final.f_principal('../Data/camion.csv', '../Data/precios.csv')

print()

print("Utilizando costo_camion.main\n")
costo_camion.f_principal('../Data/camion.csv')