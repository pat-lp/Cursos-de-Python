'''
------------------------------------------------------------------------------
Ejercicio 1.5: La pelota que rebota
------------------------------------------------------------------------------
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que
toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa rebotes.py que imprima una tabla mostrando las alturas 
que alcanza en cada uno de sus primeros diez rebotes.
------------------------------------------------------------------------------
'''
# Datos:
altura=100

print("\n-----------------\n")
print("Rebote","\tAltura")
print("\n-----------------\n")

# Se utiliza un ciclo for para realizar los 10 rebotes con la disminucion de altura
for i in range(1,11):
    altura*=(3/5)
    print(i,"\t\t",round(altura,4))
    
print("\n-----------------\n")
