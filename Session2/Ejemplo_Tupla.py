# Crear una tupla de 5 elementos de tipo diferente

mi_tupla= (1,'a','mi texto',True)

# Imprimir la Tupla

print(mi_tupla)

# Agregar mas elementos!!!

mi_tupla = mi_tupla + (8,'c')

# Imprimir nueva Tupla

print(mi_tupla)

#Acumular elementos
mi_tupla += (0,'x')

print(mi_tupla)

# Subtupla
# del segundo hasta el penultimo

print(mi_tupla[1:-1])

# Subtupla con saltos
# los elementos pares

print('Los elementos pares (comenzando en 0): ',mi_tupla[::2])

# los elementos impares

print('Los elementos pares (comenzando en 0): ',mi_tupla[1::2])


