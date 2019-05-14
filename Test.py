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