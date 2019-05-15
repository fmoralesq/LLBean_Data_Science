#1. Crear un programa que haga lo siguiente

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La lista creada es:',principal)

num1 = int(input("Dígame cuántas palabras tiene la lista:"))

if num1==num:
    print(num1)
else:
    print('Imposible!!')

#2. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La lista creada es:',principal)

buscar = input("Dígame la palabra a buscar:")

conteo = principal.count(buscar)

if conteo>0:
    print('La palabra',buscar,'aparece',conteo,'veces en la lista.')
else:
    print('La palabra',buscar,'no aparece en la lista')

#3. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la primera por la segunda en la lista

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La lista creada es:',principal)

num1 = input("Sustituir la palabra:")
num2 = input("por la palabra:")

for n, i in enumerate(principal):
    if i == num1:
        principal[n] = num2
print('La lista ahora es:',principal)

#4. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista
print('TEST!!!')
principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La lista creada es:',principal)

num1 = input("Palabra a eliminar:")
principal.remove(num1)
print('La lista ahora es:',principal)

#5. Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los nombres de la segunda lista.

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

print('La lista creada es:',principal)

num_eli = int(input("Dígame cuántas palabras quiere eliminar:"))

segunda = []
for a in range(1,num_eli+1):
    print("Dígame la palabra",a)
    b = input()
    segunda.append(b)

new_list = list(set(principal) - set(segunda))
print('La lista de palabras a eliminar es:',b)
print('La lista es ahora:',new_list)

#6. Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

inverso = principal

inverso.sort(reverse = True )

print('La lista creada es:',principal)
print('La lista inversa es:',inverso)

#7. Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).

principal = []
num = int(input("Dígame cuántas palabras tiene la lista:"))

for x in range(1,num+1):
    print("Dígame la palabra",x)
    y = input()
    principal.append(y)

dup_items = set()
uniq_items = []
for x in principal:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print('La lista creada es:',principal)
print('La lista sin repeticiones es:',dup_items)

#8. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones)

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
