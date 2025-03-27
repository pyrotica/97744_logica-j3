import os
os.system("clear")

nome_produto=str(input("digite a descrição do produto"))
quant=int(input("digite a descrição do produto"))
preco_unitario=float(input("digite a descrição do produto"))

total= quant * preco_unitario

if quant <=5:
    descoto = total * 0.02

elif quant > 5:
    desconto = total * 0.03

elif quant > 10:
    desconto = total * 0.05

total_final= total - desconto

print(f"total: {total}")
print(f"desconto: {desconto}")
print(f"total final: {total_final}")