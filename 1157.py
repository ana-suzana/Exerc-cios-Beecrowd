#Divisores I
N = int(input())

for a in range(1, N + 1):
  if N % a == 0:
    print(a)
