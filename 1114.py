#Senha Fixa
senha = 2002

while True:
  t = int(input())
  if t == senha:
    print("Acesso Permitido")
    break
  else:
    print("Senha Invalida")
