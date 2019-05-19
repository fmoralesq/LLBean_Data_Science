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

Directorio = {'01':['Francisco','Morales',89674527,'Puris',['Asma','Colitis','gripe'],['Parecetamol','Pastillita','Dexametazona']]}

num=0
while num < 8:
    num = int(input('Por favor seleccione la transaccion que desea realizar:\n1. Ingreso de un paciente nuevo\n2. Borrado de un paciente\n3. Agregar más enfermedades en un paciente en particular\n4. Agregar más medicamentos en un paciente en particular\n5. Generar reporte de las enfermedades tratadas en la clínica\n6. Generar reporte de los medicamentos entregados en la clínica\n7. Comparar 2 pacientes en particular: cuales enfermedades tienen en común. Cuales no?. Lo mismo con los medicamentos.\n8. Cerrar Directorio'))

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

    num1 = int(input('Le gustaría ver el nuevo directorio (Y/N): '))
    if num1 == 'Y':
        print(Directorio,'\n\n\n\n\n')
    else:
        print('\n\n\n\n')
elif num == 2:
    ID_del = input('Digite numero de identificacion del paciente que desea eliminar: ')
    if ID_del in Directorio is True:
        del Directorio[ID_del]

    num1 = int(input('Le gustaría ver el nuevo directorio (Y/N): '))
    if num1 == 'Y':
        print(Directorio, '\n\n\n\n\n')
    else:
        print('\n\n\n\n')

elif num == 3:
    ID_enf = input('Digite numero de identificacion del paciente que desea eliminar: ')
