import os
import time
os.system("cls || clear")
# Criar um dicionário vazio
dicionario = {}

while True:
    os.system("cls || clear")

    # Solicitar uma chave ao usuário
    chave = input("Digite a chave que deseja adicionar (ou 's' para finalizar): ").lower()
    if chave.lower() == "s":
        os.system("cls || clear")
        break

    # Solicitar um valor ao usuário
    valor = input(f"Digite o valor para a chave '{chave}': ")

    # Adicionar a chave e valor ao dicionário
    dicionario[chave] = valor

    print(f"Chave e valor adicionados: {chave}: {valor}")
    print(f"Dicionário atual: {dicionario}\n")
    time.sleep(1.8)

# Exibir o dicionário final

print("=======Dicionário final=======\n")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}\n")
    