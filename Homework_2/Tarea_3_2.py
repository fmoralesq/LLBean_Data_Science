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
print('TEST!!!')
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