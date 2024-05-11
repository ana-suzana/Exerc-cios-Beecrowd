#Salário com Bônus
nome = input()
salario = float(input())
total_vendas = float(input())

total = salario + (total_vendas * 15/100)

print(f"TOTAL = R$ {total:.2f}")
