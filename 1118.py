#Varias notas com validacao
while True:
  nota1 = float(input())
  while nota1 > 10 or nota1 < 0:
    print("nota invalida")
    nota1 = float(input())

  nota2 = float(input())
  while nota2 > 10 or nota2 < 0:
    print("nota invalida")
    nota2 = float(input())

  media = (nota1 + nota2) / 2
  print(f"media = {media:.2f}")
  novamente = int(input("novo calculo (1-sim 2-nao) "))
  if novamente != 1 and novamente != 2:
    while True:
        novamente = int(input("novo calculo (1-sim 2-nao)/n "))
        if novamente == 2 or novamente == 1:
          break
        else:
          continue
  elif novamente == 2:
    break
