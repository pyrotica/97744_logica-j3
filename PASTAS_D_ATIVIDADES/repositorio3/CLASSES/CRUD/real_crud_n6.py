import os
import time
os.system("cls || clear")
def verificar_lista_vazia(nomes):
    if not nomes:
        print("\nA lista esta vazia.")
        return True
    return False

def adicionar(nomes):
    nome= input("Digite o nome que deseja adicionar: ")
    nomes.append(nome)
    print(f"\n{nome} foi adicionado com sucesso")
    time.sleep(2.5)
    os.system("cls || clear")

def mostrar(nomes):
    if verificar_lista_vazia(nomes):
        return
    print("\n= Lista de nomes =")
    for nome in nomes:
        print(f"- {nome}")
    
def atualizar(nomes):
    if verificar_lista_vazia(nomes):
        return
    mostrar(nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in nomes:
        novo_nome = input("Digite o novo nome: ")
        indice = nomes.index(nome_antigo)
        nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}")
    else:
        print(f"O nome {nome_antigo} não foi encontrado")

def excluir(nomes):
    if verificar_lista_vazia(nomes):
        return
    mostrar(nomes)     
    nome_remover = input("Digite o nome que queira ser excluido: ")  
    if nome_remover in nomes:
        nomes.remove(nome_remover)
        print(f"{nome_remover} foi excluido com sucesso")
    else:
        print(f"O nome {nome_remover} não foi encontrado")

lista_D_nome=[]

while True:
    print("= Gerenciador de Nomes =\n")
    print(" 1- Adicionar")
    print(" 2- Lista")
    print(" 3- Atualizar")
    print(" 4- Excluir")
    print(" 5- Sair...\n")
    
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar(lista_D_nome)
        case 2:
            mostrar(lista_D_nome)
        case 3:
            atualizar(lista_D_nome)
        case 4:
            excluir(lista_D_nome)
        case 5:
            print("\nSaindo do programa")
            break
        case _:
            print("\nOpção invalida.\nTente novamente")
     
    if opcao !=1:
        print("\nEspere 5 segundos")
        time.sleep(5)
        os.system("cls || clear")