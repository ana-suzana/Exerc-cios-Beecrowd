#Aumento de salario
salario = float(input())

if 0.0 <= salario <= 400.0:
  percentual = 15
  novo_salario = salario * (1 + percentual/100)
  reajuste = salario * (percentual/100)

elif 400.01 <= salario <= 800.0:
  percentual = 12
  novo_salario = salario * (1 + percentual/100)
  reajuste = salario * (percentual/100)

elif 800.01 <= salario <= 1200.0:
  percentual = 10
  novo_salario = salario * (1 + percentual/100)
  reajuste = salario * (percentual/100)

elif 1200.01 <= salario <= 2000.0:
  percentual = 7
  novo_salario = salario * (1 + percentual/100)
  reajuste = salario * (percentual/100)

elif salario > 2000:
  percentual = 4
  novo_salario = salario * (1 + percentual/100)
  reajuste = salario * (percentual/100)

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
