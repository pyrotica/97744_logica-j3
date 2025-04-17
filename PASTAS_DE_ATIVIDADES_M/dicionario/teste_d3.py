import os
import time
os.system("cls || clear")
# Criar um dicionário vazio
dicionario = {}

# Solicitar ao usuário quantas entradas deseja adicionar
quantidade = int(input("Quantas chaves e valores você deseja adicionar ao dicionário? "))
os.system("cls || clear")

# Usar um loop for para adicionar chaves e valores
for i in range(quantidade):
    chave = input(f"Digite a {i + 1}º chave : ")
    valor = input(f"Digite o valor para a chave '{chave}': ")
    dicionario[chave] = valor  # Adicionar ao dicionário

    print(f"\nChave e valor adicionados: {chave}: {valor}\n")
    print(f"Dicionário atual: {dicionario}\n")
    time.sleep(1.8)
    os.system("cls || clear")


print("=======Dicionário final=======\n")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}\n")