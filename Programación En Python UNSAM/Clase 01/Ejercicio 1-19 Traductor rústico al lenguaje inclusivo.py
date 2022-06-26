'''
------------------------------------------------------------------------------
Ejercicio 1.19: Traductor (rústico) al lenguaje inclusivo
------------------------------------------------------------------------------
Queremos hacer un traductor que cambie las palabras masculinas de una frase 
por su versión neutra. Como primera aproximación, completá el siguiente código 
para reemplazar todas las letras 'o' que figuren en el último o anteúltimo 
caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' 
pasaría a ser 'todes somes programadores'. Guardá tu código en el archivo 
inclusive.py
------------------------------------------------------------------------------
'''

frase = 'todos somos programadores'
palabras = frase.split()
for palabra in palabras:
        if palabra[-1] =="o":
            nueva_palabra = palabra[:-1]+"e"
        elif len(palabra) >1 and palabra[-2]=="o":
            nueva_palabra = palabra[:-2]+"e"+palabra[-1]
        else:
            nueva_palabra = palabra
        print(nueva_palabra,end=" ")
        

#'todes somes programadores'
