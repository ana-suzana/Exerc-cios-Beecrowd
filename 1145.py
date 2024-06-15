#Sequência Lógica 2
entradas = input().split(" ")
X = int(entradas[0])
Y = int(entradas[1])
ultimo = 1

for i in range(1, Y, X):
  for j in range(ultimo, X + ultimo):
    print(j, end="")
    if j+1 < X + ultimo:
      print(end=" ")
  print("")
  ultimo = j + 1
