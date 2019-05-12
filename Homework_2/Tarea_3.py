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

#Cuantos pacientes llegaron en total?

conteo_pacientes = len(agenda_hospital)
print('En total llegaron ', conteo_pacientes, 'pacientes')

#Cuantas personas llegaron por dolor?
conteo_dolor = agenda_hospital. count('dolor')
print('En total llegaron ', conteo_dolor, 'pacientes')