#Triangulo
valores = input().split(" ")
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a >= c and a >= b:
  if c + b > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
  else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")

elif b >= c and b > a:
  if c + a > b:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
  else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")

elif c > b and c > a:
  if b + a > c:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
  else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
