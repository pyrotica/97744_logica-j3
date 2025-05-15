import os
import time
from dataclasses import dataclass
os.system("cls || clear")
QUANT = 3

@dataclass
class Client:
    nome_clie: str
    nasc_clie: str
    End_clie: str
clientes = []
@dataclass
class CLT:
    nome_func: str
    nasc_func: str
    Mat: str
    End_func: str
funcionarios = []
def coletar_dados_clientes(quantidade):

    for i in range(quantidade):
        print("=== INFORME OS DADOS DOS CLIENTES ===\n")
        cliente = Client(
            nome_clie=input("NOME DO CLIENTE: "),
            nasc_clie=input("DATA DE NASCIMENTO DO CLIENTE: "),
            End_clie=input("ENDEREÇO DO CLIENTE: ")
        )
        clientes.append(cliente)
        os.system("cls || clear")
    return clientes

def salvar_dados_clientes(clientes, arquivo_nome="Clientes.txt"):
    with open(arquivo_nome, "a") as arquivo:
        for cliente in clientes:
            arquivo.write(f"{cliente.nome_clie}, {cliente.nasc_clie}, {cliente.End_clie}\n")

def coletar_dados_funcionarios(quantidade):
    
    for i in range(quantidade):
        print("=== INFORME OS DADOS DOS FUNCIONÁRIOS ===\n")
        funcionario = CLT(
            nome_func=input("NOME DO FUNCIONÁRIO: "),
            nasc_func=input("DATA DE NASCIMENTO DO FUNCIONÁRIO: "),
            Mat=input("MATRÍCULA: "),
            End_func=input("ENDEREÇO DO FUNCIONÁRIO: ")
        )
        funcionarios.append(funcionario)
        os.system("cls || clear")
    return funcionarios

def salvar_dados_funcionarios(funcionarios, arquivo_nome="Funcionarios.txt"):
    with open(arquivo_nome, "a") as arquivo:
        for funcionario in funcionarios:
            arquivo.write(f"{funcionario.nome_func}, {funcionario.nasc_func}, {funcionario.Mat}, {funcionario.End_func}\n")

def exibir_arquivo(arquivo_nome, titulo):
    print(f"\t== {titulo} ==\n")
    try:
        with open(arquivo_nome, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(f"- {linha.strip()}")
    except FileNotFoundError:
        print("ARQUIVO NÃO ENCONTRADO\n")

os.system("cls || clear")


clientes = coletar_dados_clientes(QUANT)
salvar_dados_clientes(clientes)

funcionarios = coletar_dados_funcionarios(QUANT)
salvar_dados_funcionarios(funcionarios)

print("= SALVANDO OS DADOS DOS CLIENTES E FUNCIONÁRIOS =")
time.sleep(3)
os.system("cls || clear")

print("\t\n\t== Salvo com sucesso ==\t\nESPERE 5 SEGUNDOS PARA IMPRIMIR OS RESULTADOS")
time.sleep(5)
os.system("cls || clear")

exibir_arquivo("Funcionarios.txt", "FUNCIONÁRIOS")
print()
exibir_arquivo("Clientes.txt", "CLIENTES")