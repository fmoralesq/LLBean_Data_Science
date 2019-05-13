#La fila del Hospital

# Para definir la agenda del hospital
agenda_hospital = []

persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
# agregamos una persona
agenda_hospital.append(persona)
# viene otra persona
persona = ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
# agregamos otra persona
agenda_hospital.append(persona)
# suponga que vienen 5 personas mas
persona =[('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor'),]
# Podemos agregar esas personas que vienen todos de una sola vez
agenda_hospital.extend(persona)
# notemos que la impresión en pantalla está un poco sucia... lo arreglamos
for paciente in agenda_hospital:
    print(paciente)

#1. Cuantos pacientes llegaron en total?

conteo_pacientes = len(agenda_hospital)
print('En total llegaron', conteo_pacientes, 'pacientes')

#2. Cuantas personas llegaron por dolor?
Output = [item for item in agenda_hospital
          if item[5] == 'dolor']
print('LLegaron con dolor',len(Output),'pacientes')

#3. Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor. Ordene la lista desde el más adulto al más joven

odenar_x_edad = sorted(agenda_hospital, key=lambda tup: tup[3])[::-1]
for paciente in odenar_x_edad:
    print(paciente)

#4. Cuantos pacientes son mayores de edad? cuantos menores?

Mayores = [item for item in agenda_hospital
          if item[3] >= 65]
Menores = [item for item in agenda_hospital
          if item[3] < 65]
for paciente in Mayores:
    print('Los pacientes mayores de edad son:',paciente)
for paciente in Menores:
    print('Los pacientes menores de edad son:',paciente)


#5. Supong a que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor y luego por edad (mas viejo al joven), empezando por el adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.

