#Idades
i = 0
soma = 0

while True:
  idade = int(input())
  if idade < 0:
    break
  else:
    soma += idade
    i += 1

media = soma / i
print(f"{media:.2f}")
