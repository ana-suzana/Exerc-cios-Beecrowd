#Fórmula de Bhaskara
valores = input().split(" ")
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = b**2 - 4*a*c

if delta >= 0 and a != 0:
  raiz1 = (-b + delta**(1/2)) / (2 * a)
  raiz2 = (-b - delta**(1/2)) / (2 * a)
  print(f"R1 = {raiz1:.5f}")
  print(f"R2 = {raiz2:.5f}")

else:
  print("Impossivel calcular")
