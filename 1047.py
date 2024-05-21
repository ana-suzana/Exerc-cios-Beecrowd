#Tempo de jogo com minutos
entradas = input().split(" ")
h_inicial = int(entradas[0])
min_inicial = int(entradas[1])
h_final = int(entradas[2])
min_final = int(entradas[3])

duracao_horas = 0
duracao_min = 0

if h_inicial == h_final and min_inicial == min_final:
  duracao_horas = 24
  duracao_min = 0

elif h_inicial == h_final and min_inicial > min_final:
  duracao_horas = 23
  duracao_min = 60 - min_inicial + min_final

elif h_inicial == h_final and min_inicial < min_final:
  duracao_horas = 0
  duracao_min = min_final - min_inicial

else:
  if h_inicial > h_final and min_inicial > min_final:
    duracao_horas = ((24 - h_inicial) + h_final) -1
    duracao_min = (60 - min_inicial) + min_final

  elif h_inicial > h_final and min_inicial < min_final:
    duracao_horas = (24 - h_inicial) + h_final
    duracao_min = min_final - min_inicial

  elif h_inicial < h_final and min_inicial > min_final:
    duracao_horas = h_final - h_inicial - 1
    duracao_min = (60 - min_inicial) + min_final

  elif h_inicial < h_final and min_inicial < min_final:
    duracao_horas = h_final - h_inicial
    duracao_min = min_final - min_inicial

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_min} MINUTO(S)")
