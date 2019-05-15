principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La primera lista creada es:',principal)

num_eli = int(input("Dígame cuántas palabras quiere eliminar:"))

segunda = []
for a in range(1,num_eli+1):
    print("Dígame la palabra",a)
    b = input()
    segunda.append(b)

print('La segunda lista creada es:',segunda)

duplicados = list(set(principal) & set(segunda))

print('Palabras que aparecen en las dos listas:',duplicados)

a = set(principal)
b = set(segunda)
c = list(b - a)
d = list(a - b)

print('Palabras que aparecen en solo lista 1',d)
print('Palabras que aparecen en solo lista 2',c)

e = list(a+b)

print('Palabras que aparecen en ambas listas ',e)