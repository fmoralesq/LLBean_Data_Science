#Cual es el promedio

pixel = [0.6,0.3,0.4]
suma = pixel[0]+pixel[1]+pixel[2]
avg = suma/len(pixel)
print(avg)

# Otra solucion
# mediante ciclos

p = 0
for numero in pixel:
    p += numero
p = p/len(pixel)
print(p)

# Otra solucion
# mediante funcion suma

mi_suma = sum(pixel)
mi_avg = mi_suma/len(pixel)
print(mi_avg)

# Otra solucion
# en una linea

mi_avg = sum(pixel)/len(pixel)
print(mi_avg)

# Definir si es blanco o negro

if mi_avg > 0.5:
    print('Blanco')
else:
    print('Negro')

