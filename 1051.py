#Imposto de Renda
salario = float(input())

if salario >= 0 and salario <= 2000:
  print("Isento")

elif salario > 2000 and salario <= 3000:
  resto = salario - 2000
  imposto = resto * (0.08)
  print(f"R$ {imposto:.2f}")

elif salario > 3000 and salario <= 4500:
  resto = salario - 2000 #parte isenta
  if resto <= 1000:
    imposto = resto * (0.08)
    print(f"R$ {imposto:.2f}")
  else:
    resto_sem_milhar = resto - 1000
    imposto = (1000 * (0.08)) + (resto_sem_milhar * (0.18))
    print(f"R$ {imposto:.2f}")

else:
  resto = salario - 2000 #valor isento
  resto_1000 = resto - 1000 #valor que ficaria entre 2000 e 3000
  resto_1500 = resto_1000 - 1500 #valor entre 3000 e 4500

  # 1º imposto sobre os 1000; 2º imposto sobre os 1500; 3º imposto sobre a parte que sobra acima de 4500
  imposto = (1000 * (0.08)) + (1500 * (0.18)) + (resto_1500 * (0.28))
  print(f"R$ {imposto:.2f}")
