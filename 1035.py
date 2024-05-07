#Teste de seleção 1

numeros = input().split(" ")
A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])
D = int(numeros[3])

somaCD = C + D 
somaAB = A + B
positivo = C >= 0 and D >= 0
parA = A % 2 == 0 

if B > C and D > A and somaCD > somaAB and positivo and parA:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")