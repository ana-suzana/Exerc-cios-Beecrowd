#Soma de Ímpares consecutivos III
N = int(input())

for contador in range(N):
  i = 0
  impares = 0
  soma = 0
  valores = input().split(" ")
  X = int(valores[0])
  Y = int(valores[1])

  while impares < Y:
    valor = X + i
    if valor % 2 != 0:
      impares += 1
      soma += valor
    i += 1

  print(soma)
