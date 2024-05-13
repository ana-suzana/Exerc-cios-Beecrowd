#O maior
numeros = input().split(" ")
num1 = int(numeros[0])
num2 = int(numeros[1])
num3 = int(numeros[2])

if num1 > num2 and num1 > num3:
  print(f"{num1} eh o maior")

elif num2 > num1 and num2 > num3:
  print(f"{num2} eh o maior")

elif num3>num1 and num3>num2:
  print(f"{num3} eh o maior")
