#Multiplos de 13
X = int(input())
Y = int(input())
soma = 0

if X > Y:
  for i in range(Y, X + 1):
    if i % 13 != 0:
      soma += i
else:
  for i in range(X, Y + 1):
    if i % 13 != 0:
      soma += i

print(soma)
