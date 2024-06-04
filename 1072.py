# Intervalo 2
n = int(input())
contador = 0
i = 0
o = 0

while contador < n:
  x = int(input())
  if 10 <= x <= 20:
    i = i + 1
  else:
    o = o + 1

  contador +=1

print(f"{i} in\n{o} out")
