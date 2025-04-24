import os
import time
os.system("cls || clear")
# Criar um dicionário vazio
dicionario = {}
contador=0

while True:
    os.system("cls || clear")

    # Solicitar uma chave ao usuário
    chave = input("Digite a chave que deseja adicionar (ou 's' // '0' para finalizar): ").lower()
    if chave.lower() == "s" or chave.lower()=="0":
        os.system("cls || clear")
        break

    # Solicitar um valor ao usuário
    valor = input(f"Digite o valor para a chave '{chave}': ")

    # Adicionar a chave e valor ao dicionário
    dicionario[chave] = valor

    print(f"Chave e valor adicionados: {chave}: {valor}")
    print(f"Dicionário atual: {dicionario}\n")
    time.sleep(1.8)
    contador+=1
#se for adicionado pelo menos 1 chave\valor
if contador>0:
 for chave, valor in dicionario.items():
    print(f"{chave}: {valor}\n")
 print(dicionario.keys())
 print(dicionario.values())
#se nao for adicionado nem uma chave\valor
else:
   print("___NEM UM VALOR ADICIONADO___")