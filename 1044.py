#Multiplos
entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

if a >= b:
  multiplos = a % b == 0
  if multiplos == True:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")

else:
  multiplos = b % a == 0
  if multiplos == True:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
