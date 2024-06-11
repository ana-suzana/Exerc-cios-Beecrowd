#Converter para Hexadecimal
hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
V = int(input())
resultado = list()

while V > 0:
    resultado.append(hexa[(V % 16)])
    V = V // 16
for i in range(len(resultado)-1,-1,-1): #inverte a lista
    if i == 0:
      print(resultado[i])
    else:
      print(resultado[i], end="")
