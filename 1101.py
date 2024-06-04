# Sequência de Números e Soma
entradas = input().split(" ")
m = int(entradas[0])
n = int(entradas[1])

while m > 0 and n > 0:
  soma1 = 0
  soma2 = 0
  if m > n:
    for i in range(n, m + 1):
      print(i, end=" ")
      soma1 += i
    print(f"Sum={soma1}")
  elif m < n:
    for i in range(m, n+ 1):
      print(i, end=" ")
      soma2 += i
    print(f"Sum={soma2}")

  entradas = input().split(" ")
  m = int(entradas[0])
  n = int(entradas[1])
