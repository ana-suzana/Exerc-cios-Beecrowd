#Fatorial simples
N = int(input())
fatorial = 1

for a in range(N, 0, -1):
  fatorial *= a

print(fatorial)
