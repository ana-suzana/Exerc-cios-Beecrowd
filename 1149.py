#Somando Inteiros Consecutivos
entradas = input().split(" ")

A = int(entradas[0])
N = int(entradas[-1])

soma = 0

for i in range(0, N):
  soma = soma + A + i

print(soma)
