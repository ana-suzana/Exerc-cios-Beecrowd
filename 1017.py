#Gasto de combustivel
tempo_gasto = int(input())
v_media = int(input())

distancia = v_media * tempo_gasto
qtd_litros = distancia / 12

print(f"{qtd_litros:.3f}")
