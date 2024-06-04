# Experiencias
n = int(input())
i = 0
qtd_rato = 0
qtdC = 0
qtd_s = 0
total_cobaia = 0

while i < n:
  cobaia = input().split(" ")
  qtd = int(cobaia[0])
  tipo = cobaia[1]
  if tipo == "R":
    qtd_rato = qtd_rato + qtd
  elif tipo == "C":
    qtdC = qtdC + qtd
  elif tipo == "S":
    qtd_s = qtd_s + qtd

  total_cobaia = total_cobaia + qtd
  i += 1

pC = (qtdC / total_cobaia) * 100
pR = (qtd_rato / total_cobaia) * 100
pS = (qtd_s / total_cobaia) * 100

print(f"Total: {total_cobaia} cobaias")
print(f"Total de coelhos: {qtdC}\nTotal de ratos: {qtd_rato}\nTotal de sapos: {qtd_s}")
print(f"Percentual de coelhos: {pC:.2f} %\nPercentual de ratos: {pR:.2f} %\nPercentual de sapos: {pS:.2f} %")
