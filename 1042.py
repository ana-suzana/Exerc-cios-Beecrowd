#Sort simples
valores = input().split(" ")
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if a <= b and a <= c:
  print(a)
  if b >= c:
    print(c)
    print(b)
  else:
    print(b)
    print(c)

elif b <= a and b <= c:
  print(b)
  if a >= c:
    print(c)
    print(a)
  else:
    print(a)
    print(c)

else:
  print(c)
  if b >= a:
    print(a)
    print(b)
  else:
    print(b)
    print(a)

print(f"\n{a}\n{b}\n{c}")
