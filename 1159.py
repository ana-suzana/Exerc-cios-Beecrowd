#Soma de pares consecutivos
while True:
  pares = 0 #quantidade de números pares
  i = 0 #incremento para X
  soma = 0 #soma dos pares
  X = int(input())
  if X == 0:
    break
  else:
    while pares < 5:
      valor = X + i
      if valor % 2 == 0:
        soma += valor
        pares += 1
      i += 1
    print(soma)
