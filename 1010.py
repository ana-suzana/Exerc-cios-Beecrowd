#Calculo simples
entradas = input().split(" ")
cod1 = int(entradas[0])
qtd1 = int(entradas[1])
valor_uni1 = float(entradas[2])

entradas2 = input().split(" ")
cod2 = int(entradas2[0])
qtd2 = int(entradas2[1])
valor_uni2 = float(entradas[2])

total = qdt1 * valor_uni1 + qtd2 * valor_uni2
print(f"VALOR A PAGAR: R$ {total:.2f}")
