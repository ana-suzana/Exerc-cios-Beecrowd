# Soma de Ímpares Consecutivos II
N = int(input())
j = 0
lista_somas= []
while j < N:
  soma = 0
  entradas = input().split(" ")
  x = int(entradas[0])
  y = int(entradas[1])

  if y > x:
    for i in range(x + 1, y):
      if i % 2 != 0:
        soma += i
    lista_somas.append(soma)
  elif y < x:
    for i in range(y +1, x):
      if i % 2 != 0:
        soma += i
    lista_somas.append(soma)
  else:
    lista_somas.append(soma)
  j += 1

l = 0
while l < len(lista_somas):
  print(lista_somas[l])
  l += 1
