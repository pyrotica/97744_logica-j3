import os
import time
os.system("cls || clear")
from dataclasses import dataclass
def verificar_lista_vazia(nomes):
    if not nomes:
        print("\nA lista esta vazia.")
        return True
    return False

def adicionar(nomes):
    clt= input("Digite o nome do funcionario que deseja adicionar: ")
    nasc_clt=input("Digite a data de nascimento: ")
    cpf_clt=input("Digite o CPF do funcionario: ")
    funcion_clt=input("Sua função: ")
    nomes.append(clt)
    nomes.append(nasc_clt)
    nomes.append(cpf_clt)
    nomes.append(funcion_clt)
    print(f"\n{clt} foi adicionado a lista de funcionarios com sucesso")
    time.sleep(2.5)
    os.system("cls || clear")

def mostrar(nomes):
    if verificar_lista_vazia(nomes):
        return
    print("\n= Lista de nomes =")
    for clt in nomes:
        print(f"- {clt}")
    
def atualizar(nomes):
    if verificar_lista_vazia(nomes):
        return
    mostrar(nomes)
    clt_antigo = input("Digite o nome que deseja atualizar: ")
    if clt_antigo in nomes:
        clt_nome = input("Digite o novo nome: ")
        indice = nomes.index(clt_antigo)
        nomes[indice] = clt_nome
        print(f"{clt_antigo} foi atualizado para {clt_nome}")
    else:
        print(f"O nome {clt_antigo} não foi encontrado")

def demitir(nomes):
    if verificar_lista_vazia(nomes):
        return
    mostrar(nomes)     
    clt_apagar = input("Digite o funcionario que queira demitir: ")  
    if clt_apagar in nomes:
        nomes.remove(clt_apagar)
        print(f"{clt_apagar} foi excluido com sucesso")
    else:
        print(f"O nome {clt_apagar} não foi encontrado")
    
print("\t\t==== EMPRESA DO MIGUES ====")
time.sleep(3.57)
os.system("cls || clear")
lista_D_nome=[]
QUANT=int(input("Digite o numero de funcionarios que deseja adicionar: "))
os.system("cls || clear")
if QUANT>0:
    @dataclass
    class CLT:
        clt: str
        nasc_clt: str
        cpf_clt: str
        funcion_clt: str
    liat_D_funcionarios=[]


    for i in range(QUANT):
     print("===INFORME OS DADOS DOS FUNCIONARIOS===\n")
     funcionarios=CLT(
        clt=input("NOME DO FUNCIONARIO: "),
        nasc_clt=input("DATA DE NASCIMENTO DO FUNCIONARIO: "),
        cpf_clt=input("CPF: "),
        funcion_clt=input("SUA FUNÇÃO: ")
    )
    liat_D_funcionarios.append(funcionarios)
    os.system("cls || clear")
    
    while True:
        print("= Gerenciador de Funcionarios =\n")
        print(" 1- Adicionar funcionario")
        print(" 2- Lista de funcionarios")
        print(" 3- Atualizar funcionario")
        print(" 4- Demitir funcionario")
        print(" 5- Sair...\n")
        
        opcao = int(input("Digite uma das opções acima: "))
        os.system("cls || clear")

        match opcao:
            case 1:
                adicionar(liat_D_funcionarios)
            case 2:
                mostrar(liat_D_funcionarios)
            case 3:
                atualizar(liat_D_funcionarios)
            case 4:
                demitir(liat_D_funcionarios)
            case 5:
                print("\nSaindo do programa")
                break
            case _:
                print("\nOpção invalida.\nTente novamente")
        
        if opcao !=1:
            print("\nEspere 5 segundos")
            time.sleep(5)
            os.system("cls || clear")

else:
    print("\tQuantidade inserida invalida\n\t\tCodigo encerrado")