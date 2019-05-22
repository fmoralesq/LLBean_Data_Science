'''
Directorio de pacientes de una clínica.
Se propone crear una aplicación escrita en Python que permita la gestión de pacientes de una clínica.

a saber información clásica de paciente como:

identificación
Nombre
Apellido
teléfono
dirección
lista de enfermedades tratadas
lista de medicamentos que toma
Operaciones:

Ingreso de un paciente nuevo
Borrado de un paciente
Agregar más enfermedades en un paciente en particular
Agregar más medicamentos en un paciente en particular
Generar reporte de las enfermedades tratadas en la clínica
Generar reporte de los medicamentos entregados en la clínica
Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.
Consideraciones:

La lista inicial de pacientes puede estar escrito en el código asi como su información. La implementación puede ser abierta: puede ser que cada paciente sea creado por una clase o simplemente cada paciente sea un diccionario con toda la información solicitada.

'''

#LLamar diccionario original

Directorio = {'01':['Francisco','Morales',89674527,'Puris',['Asma','Colitis','gripe'],['Parecetamol','Pastillita','Dexametazona']]}

#Crear ciclo para determinar que tarea del menu se necesita realizar

num=0
while num < 8:
    num = int(input('Por favor seleccione la transaccion que desea realizar:\n1. Ingreso de un paciente nuevo\n2. Borrado de un paciente\n3. Agregar más enfermedades en un paciente en particular\n4. Agregar más medicamentos en un paciente en particular\n5. Generar reporte de las enfermedades tratadas en la clínica\n6. Generar reporte de los medicamentos entregados en la clínica\n7. Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.\n8. Cerrar Directorio'))

# Ingreso de un paciente nuevo

    if num == 1:
        ID_nuevo = input('Digite numero de identificacion del paciente nuevo: ')
        Nombre = input('Digite Nombre del paciente nuevo: ')
        Apellido = input('Digite Apellido del paciente nuevo: ')
        Tel = input('Digite numero de telefono del paciente nuevo: ')
        Direccion = input('Digite direccion del paciente nuevo: ')
        enfermedades = input('Enliste las enfermedades tratadas en la clinica separadas por una ",": ')
        Lista_enfermedades = list(enfermedades.split(','))
        Medicamentos = input('Enliste los medicamentos recetados en la clinica separados por una ",": ')
        Lista_Medicamentos = list(Medicamentos.split(','))

        Directorio[ID_nuevo] = [Nombre,Apellido,Tel,Direccion,Lista_enfermedades,Lista_Medicamentos]

        num1 = input('Le gustaría ver el nuevo directorio (Y/N): ')
        if num1 == 'Y':
            print(Directorio,'\n\n\n\n\n')
        else:
            print('\n\n\n\n')

    # Borrado de un paciente

    elif num == 2:
        ID_del = input('Digite numero de identificacion del paciente que desea eliminar: ')
        del Directorio[ID_del]

        num1 =input('Le gustaría ver el nuevo directorio (Y/N): ')
        if num1 == 'Y':
            print(Directorio, '\n\n\n\n\n')
        else:
            print('\n\n\n\n')

    # Agregar más enfermedades en un paciente en particular

    elif num == 3:
        ID_enf = input('Digite numero de identificacion del paciente que necesita agregar mas enfermedades: ')
        lista1 = list(Directorio[ID_enf])
        mi_lista_enf = lista1[4]

        nuevas_enfer = input('Enliste las nuevas enfermedades tratadas en la clinica separadas por una ",": ')
        Lista_nuevasE = nuevas_enfer.split(',')

        mi_lista_enf.extend(Lista_nuevasE)

        num1 = input('Le gustaría ver el nuevo directorio (Y/N): ')
        if num1 == 'Y':
            print(Directorio, '\n\n\n\n\n')
        else:
            print('\n\n\n\n')


    #Agregar más medicamentos en un paciente en particular
    elif num == 4:
        ID_med = input('Digite numero de identificacion del paciente que necesita agregar mas medicamentos: ')
        lista1 = list(Directorio[ID_med])
        mi_lista_med = lista1[5]

        nuevas_med = input('Enliste las nuevas medicinas dadas en la clinica separadas por una ",": ')
        Lista_nuevasM = nuevas_med.split(',')

        mi_lista_med.extend(Lista_nuevasM)

        num1 = input('Le gustaría ver el nuevo directorio (Y/N): ')
        if num1 == 'Y':
            print(Directorio, '\n\n\n\n\n')
        else:
            print('\n\n\n\n')

    #Generar reporte de las enfermedades tratadas en la clínica
    elif num == 5:
        p = []
        for k in Directorio.values():
            lista_enf = k[4]
            p = p + lista_enf
            rep_enf = set(p)
        print('El reporte de enfermedades es:\n',rep_enf)


    #Generar reporte de los medicamentos entregados en la clínica
    elif num == 6:
        p = []
        for k in Directorio.values():
            lista_med = k[5]
            q = q + lista_med
            rep_med = set(q)
        print('El reporte de medicinas es:\n', rep_med)


    #Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos
    elif num == 7:
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

        print('Las enfermedades que tienen en comun son:',enf_comun,'\nLos medicamentos que tienen en comun son:',med_comun)

