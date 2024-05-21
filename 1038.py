#Lanche
entradas = input().split(" ")
cod = int(entradas[0])
qtd = int(entradas[1])

if cod == 1:
  valor = qtd * 4.0

elif cod == 2:
  valor = qtd * 4.5

elif cod == 3:
  valor = qtd * 5

elif cod == 4:
  valor = qtd * 2

else:
  valor = qtd * 1.5

print(f"Total: R$ {valor:.2f}")
