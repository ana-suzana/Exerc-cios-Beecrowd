entrada = int(input())

print(f"{entrada // 365} ano(s)") 
resto_anos = entrada % 365
print(f"{resto_anos // 30} mes(es)") 
print(f"{resto_anos % 30} dia(s)")
