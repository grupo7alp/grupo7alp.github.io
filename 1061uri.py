diaInicial = int(input().split() [1])
#Agora criaremos o split para separar a lista contendo as h/m/s com ":".
hora = input().split(" : ")
#E criaremos uma lista para guardar as horas,min e seg.
hora_ini = int(hora[0])
minuto_ini = int(hora[1])
segundo_ini = int(hora[2])
#O mesmo faremos para o dia final
diaFinal = int(input().split() [1])

hora = input().split(" : ")
hora_final = int(hora[0])
minuto_final = int(hora[1])
segundo_final = int(hora[2])

#Agora calculamos o Dia e a Hora:
dias = diaFinal - diaInicial
horas = hora_final - hora_ini

#Só que temos um problema; se a hora final for menor que a hora iniciar, ele diminuira 1 dia.
#Então resolveremos com IF

#Se horas for menor que 0, então quer dizer que a hora final é menor que a hora inicial.
if horas < 0:
    horas += 24
    dias -= 1

minutos = minuto_final - minuto_ini
if minutos < 0:
    minutos += 60
    horas -= 1
segundos = segundo_final - segundo_ini
if segundos < 0:
    segundos += 60
    minutos -= 1

print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(segundos))





