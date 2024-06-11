# O escolhido
n = int(input())
matricula = list()
nota = list()

for _ in range(n):
  entradas = input().split(" ")
  m = int(entradas[0])
  nota_aluno = float(entradas[1])
  matricula.append(m)
  nota.append(nota_aluno)

i = 1
maior_nota = nota[0]
posicao_matricula = matricula[0]

while True:
  if nota[i] > maior_nota:
    maior_nota = nota[i]
    posicao_matricula = i
  if i == n-1:
    break
  i+=1

if maior_nota >= 8:
  print(matricula[posicao_matricula])
else:
  print("Minimum note not reached")
