#Crescimento populacional
T = int(input())
i = 0

while i < T:
  y = 0
  values = input().split(" ")
  PA = int(values[0])
  PB = int(values[1])
  G1 = float(values[2])
  G2 = float(values[3])

  while PA <= PB:
    PA = PA + ((PA * (G1/100))//1)
    PB = PB + ((PB * (G2/100))//1)
    y += 1
  if y > 100:
    print("Mais de 1 seculo.")
  else:
    print(f"{y} anos.")
  i += 1
