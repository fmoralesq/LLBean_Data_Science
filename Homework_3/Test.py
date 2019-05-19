Directorio = {'01':['Francisco','Morales',89674527,'Puris',['Asma','Colitis','gripe'],['Parecetamol','Pastillita','Dexametazona']],'02':['Fran','Mora',89674528,'Puris',['Colitis','gripe'],['Parecetamol','Dexametazona']]}
pass
ID_1 = input('Digite numero de identificacion del primer paciente que desea comparar: ')
ID_2 = input('Digite numero de identificacion del segundo paciente que desea comparar: ')

lista1 = list(Directorio[ID_1])
mi_lista_enf1 = set(lista1[4])
mi_lista_med1 = set(lista1[5])

lista2 = list(Directorio[ID_2])
mi_lista_enf2 = set(lista2[4])
mi_lista_med2 = set(lista2[5])

enf_comun = mi_lista_enf1 & mi_lista_enf2
med_comun = mi_lista_med1 & mi_lista_med2

print('Las enfermedades que tienen en comun son:', enf_comun, '\nLos medicamentos que tienen en comun son:', med_comun)

print(Directorio)