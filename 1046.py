#Tempo de jogo
entradas = input().split(" ")
h_inicial = int(entradas[0])
h_final = int(entradas[1])

if h_inicial > h_final:
  duracao = (24 - h_inicial) + h_final

elif h_inicial == h_final:
  duracao = 24
else:
  duracao = h_final - h_inicial
print(f"O JOGO DUROU {duracao} HORA(S)")
