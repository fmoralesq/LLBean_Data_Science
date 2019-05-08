# Cual es el maximo para la lista

lista = [44,11,15,29,53,12,30]

max = 0
for num in lista:
    if num > max:
        max = num

print(max)


# con max

print(max(lista))
