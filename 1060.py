#Numeros positivos
i = 0
par = 0

while i < 6:
  n = float(input())
  if n > 0:
    par = par + 1
  i += 1
print(f"{par} valores positivos")
