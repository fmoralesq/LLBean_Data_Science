#Parte 1: (Promedio)
mi_lista = [5,6,10,13,3,4]
mi_suma = sum(mi_lista)
mi_avg = mi_suma/len(mi_lista)
print(mi_avg)

import statistics
avg = statistics.mean(mi_lista)
print(avg)

#Parte 2: Grupo con mayor alturas

#Asignar grupos
grupo1 = [177,145,167,190,140,150,180,130]
grupo2 = [165,176,145,189,170,189,159,190]
grupo3 = [145,136,178,200,123,145,145,134]
grupo4 = [201,110,187,175,156,165,156,135]

#Calcular Promedios de los grupos

max_1 = max(grupo1)
max_2 = max(grupo2)
max_3 = max(grupo3)
max_4 = max(grupo4)

max_tot = max(max_1,max_2,max_3,max_4)

if max_tot== max_1:
    print('La altura maxima se encuentra en grupo 1 y es:',max_1)
else:
    if max_tot == max_2:
        print('La altura maxima se encuentra en grupo 2 y es:', max_2)
    else:
        if max_tot == max_3:
            print('La altura maxima se encuentra en grupo 3 y es:', max_3)
        else:
            print('La altura maxima se encuentra en grupo 4 y es:', max_4)