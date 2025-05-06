import os
os.system("cls || clear")

preco=int(input("Digite o preço do produto: "))

def des_acre(): 
    

 if preco <100:
  preco_inflacionado=(preco*1.1)

 elif preco>=100:
    preco_inflacionado=(preco*1.2)
 return preco_inflacionado

preco_inflacionado=des_acre()

print(f"valor acrecimado: {preco_inflacionado:.0f}")
