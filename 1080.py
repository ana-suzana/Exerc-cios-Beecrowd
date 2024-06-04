# Maior e posicao
i = 1
maior = 0 #Isso porque 0 é o menor valor possível de se obter dentro dos requisitos do programa
while i <= 100:
  n = int(input())
  if n > maior:
    maior = n
    posicao = i
  i += 1
print(maior)
print(posicao)
