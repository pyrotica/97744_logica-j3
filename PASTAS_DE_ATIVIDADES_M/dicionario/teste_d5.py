import os
import time
os.system("cls || clear")

# Função para adicionar chaves e valores ao dicionário
def adicionar_ao_dicionario():
    dicionario = {}  # Cria um dicionário vazio

    while True:
        os.system("cls || clear")

        # Solicita ao usuário que insira uma chave
        chave = input("Digite a chave (ou 's' para finalizar): ")
        if chave.lower() == "s":
            break  # Sai do loop se o usuário digitar "sair"

        # Solicita ao usuário que insira o valor
        valor = input(f"Digite o valor para a chave '{chave}': ")

        # Adiciona a chave e o valor ao dicionário
        dicionario[chave] = valor
        print(f"Chave e valor adicionados: {chave}: {valor}\n")
        time.sleep(1.8)

    return dicionario  # Retorna o dicionário final


# Chamar a função e receber o dicionário final
dicionario = adicionar_ao_dicionario()
os.system("cls || clear")
print("=======Dicionário final=======\n")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}\n")