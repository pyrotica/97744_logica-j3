import os
os.system("cls || clear")
import time
from dataclasses import dataclass



@dataclass
class Cliente:
    nome: str
    EMAIL: str
    telefone: int

lista_pessoas=[]
QUANT=2

print("===INFORME OS DADOS===\n")

cliente=Cliente(
    nome=input("NOME: "),
    EMAIL=input("EMAIL: "),
    telefone=input("TELEFONE: ")
    )
lista_pessoas.append(cliente)   
print()
os.system("cls || clear")
    


print("===EXIBIR RESULTADOS===\n")

for clientes in lista_pessoas:
    print("===DADOS DO USUARIO===\n")
    print(f"NOME: {cliente.nome}")
    print(f"EMAIL: {cliente.EMAIL}")
    print(f"TEFONE: {cliente.telefone}\n\n")

print("= SALVANDO OS DADOS DOS CLIENTES =")
time.sleep(3)
nome_arquivo= "dados_clientes.txt"

with open(nome_arquivo, "w") as arquivo:
    for linha in lista_pessoas:
     arquivo.write(f"{cliente.nome},{cliente.EMAIL},{cliente.telefone}\n")

print("\nSalvo com sucesso")
