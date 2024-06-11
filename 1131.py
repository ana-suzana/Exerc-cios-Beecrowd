#Grenais
jogos = 0
vitoriasInter = 0
vitoriasGremio = 0
empates = 0
novamente = 1

while novamente == 1:
  gols = input().split(" ")
  golsInter = int(gols[0])
  golsGremio = int(gols[1])

  if golsInter > golsGremio:
    vitoriasInter += 1
  elif golsInter < golsGremio:
    vitoriasGremio += 1
  else:
    empates += 1

  jogos += 1
  novamente = int(input("Novo grenal (1-sim 2-nao) \n"))
  if novamente != 1:
    break

print(f"{jogos} grenais")
print(f"Inter:{vitoriasInter}")
print(f"Gremio:{vitoriasGremio}")
print(f"Empates:{empates}")

if vitoriasInter > vitoriasGremio:
  print("Inter venceu mais")
elif vitoriasInter < vitoriasGremio:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")
