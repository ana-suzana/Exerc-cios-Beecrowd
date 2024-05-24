#Notação científica 
def expoente(num):
  if num < 10:
    return "0"+str(num)
  else:
    return num

X = float(input())

if 1 <= X < 10:
  print(f"+{X:.4f}E+00")

elif X >= 10:
  inteiro = X // 1 
  casas = str(int(inteiro))
  exp = len(casas) - 1
  notacao = X / 10**exp
  print(f"+{notacao:.4f}E+{expoente(exp)}")

elif X == 0 or X == -0:
    valor = str(X)
    if valor[0] == "-":
      print("-0.0000E+00")
    else:
      print(f"+0.0000E+00")

elif -1 < X < 0 or 0 < X < 1:#
  if X < 0:
    valor = X * (-1)
    sinal ="-"
  else:
    valor = X
    sinal = "+"
  i = 0
  while True:
    valor = valor * 100
    i+=2
    if valor > 10:
      valor = valor / 10
      i -= 1
    if valor >= 1:
      print(f"{sinal}{valor:.4f}E-{expoente(i)}")
      break
      
elif -10 < X <= -1:
    print(f"-{X:.4f}E+00")

else:
  inteiro = (X // 1) * (-1) 
  casas = str(int(inteiro))
  exp = len(casas) - 1
  notacao = X / 10**exp
  print(f"{notacao:.4f}E+{expoente(exp)}")
